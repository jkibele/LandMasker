from osgeo import gdal, ogr
from osgeo.gdalconst import *
import os
import numpy as np
from scipy.ndimage.measurements import label

class RasterDS(object):
    """
    We'll be getting raster layers as Qgis raster layers but we need to do gdal
    stuff with them. This object will let us do that and let us make our own
    methods. It'll also take a file path to a tif or lan.
    """
    def __init__(self, rlayer, overwrite=False):
        self.rlayer = rlayer
        self.overwrite = overwrite
        try:
            self.file_path = str( rlayer.publicSource() )
        except AttributeError:
            self.file_path = rlayer
        self.gdal_ds = self.__open_gdal_ds()
        # store the text portion of the file extension in case we need the file type
        self.file_type = os.path.splitext(self.file_path)[-1].split(os.path.extsep)[-1]
        
    def __open_gdal_ds(self):
        """return a gdal datasource object"""
        # register all of the GDAL drivers
        gdal.AllRegister()
    
        # open the image
        img = gdal.Open(self.file_path, GA_ReadOnly)
        if img is None:
            print 'Could not open %s. This file does not seem to be one that gdal can open.' % self.file_path
            return None
        else:
            return img
            
    @property
    def band_array(self):
        """Take a raster datasource and return a band array. Each band is read
        as an array and becomes one element of the band array."""
        img = self.gdal_ds
        for band in range(1,img.RasterCount + 1):
            barr = img.GetRasterBand(band).ReadAsArray()
            if band==1:
                bandarr = np.array([barr])
            else:
                bandarr = np.append(bandarr,[barr],axis=0)
        return bandarr
            
    @property
    def pyplot_band_array(self):
        """Take a raster datasource and return a band array. Shape will be 
        N x Rows x Columns where N is the number of bands."""
        bandarr = self.gdal_ds.ReadAsArray()
        return bandarr

    def output_file_path(self, add_on=None):
        """
        Return a file path for output. Assume that we'll output same file 
        extension.
        
        :param add_on: A str that you want appended to the file name before
        the file extension.
        :type add_on: str
        """
        f_ext = self.file_type
        fname = self.file_path
        if add_on:
            fname = fname.replace( os.path.extsep + f_ext, add_on + os.path.extsep + f_ext )
            
        if self.overwrite:
            return fname 
        else:
            add_num = 0
            while os.path.exists(fname):
                add_num += 1
                if add_num==1:
                    fname = fname.replace( os.path.extsep + f_ext, '_%i' % add_num + os.path.extsep + f_ext )
                else:
                    old = '_%i.%s' % ( add_num - 1, f_ext )
                    new = '_%i.%s' % ( add_num, f_ext )
                    fname = fname.replace( old, new )
            return fname    
    
    def new_image_from_array(self,bandarr,outfilename=None,dtype=GDT_Float32,no_data_value=-99):
        """
        Save an image like self from a band array.
        """
        if not outfilename:
            outfilename = self.output_file_path()
        output_gtif_like_img(self.gdal_ds, bandarr, outfilename, no_data_value=no_data_value, dtype=dtype)
        return RasterDS(outfilename)
        
    def apply_mask_band(self, maskband):
        """
        Return a band array of self with all pixels zeroed where mask is zero.
        
        :param maskband: Numpy Array of zeros and ones. The shape must be
        compatible with self's shape. If self.pyplot_band_array.shape = 
        N x R X C, the maskband.shape must be R x C. (N is the number of bands)
        :type maskband: numpy.ndarray
        """
        bandarr = self.pyplot_band_array
        return bandarr * maskband
        
    def apply_mask_image(self, maskimg):
        """
        Return a band array of self with all pixels zeroed where mask is zero.
        
        :param maskimg: The mask image.
        :type maskimg: RasterDS
        """
        maskband = maskimg.gdal_ds.ReadAsArray()
        return self.apply_mask_band(maskband)
        
    def new_masked_image(self, mask, outfilename=None):
        """
        Write out a new image masked by a mask RasterDS or array.
        
        :param mask: The mask image or band.
        :type mask: RasterDS or mask array.
        
        :param outfilename: The path for the new image.
        :type outfilename: str
        """
        if mask.__class__.__name__=='RasterDS':
            new_bandarr = self.apply_mask_image(mask)
        else:
            new_bandarr = self.apply_mask_band(mask)
        if not outfilename:
            outfilename = self.output_file_path(add_on="_masked")
        return self.new_image_from_array( new_bandarr, outfilename=outfilename, dtype=GDT_UInt16)
        
    
    def ward_cluster_land_mask(self,threshold=50):
        """
        Try to seperate land from water using scikits-learn ward clustering. The 
        simple land_to_zeros method above does not distinguish shadow pixels on land
        from water pixels. The Ward clustering conectivity constraint should take
        care of that.
        """
        from sklearn.cluster import Ward    
        from sklearn.feature_extraction.image import grid_to_graph
        import time
        # Get the last band. I'm assuming the last band will be the longest
        # wavelength.
        band = self.band_array[-1]
        # zero out pixels that are above the threshold
        band[np.where(band > threshold)] = 0
        
        X = np.reshape(band, (-1,1))
        connectivity = grid_to_graph(*band.shape)
        
        st = time.time()
        n_clusters = 2
        ward = Ward(n_clusters=n_clusters, connectivity=connectivity).fit(X)
        label = np.reshape(ward.labels_, band.shape)
        print "Elaspsed time: ", time.time() - st
        return label
        
    def simple_land_mask(self,threshold=50):
        """
        Return an array of ones and zeros that can be used as a land mask. Ones
        will be water and zeros will be land. This method fails to mask out
        shadows.
        """
        # get the last band assuming it's the longest wavelength
        band = self.gdal_ds.ReadAsArray()[-1]
        # make a copy so we can modify it for output and still have the 
        # original values to test against
        output = band.copy()
        # pixels at or bellow threshold to ones
        output[np.where(band <= threshold)] = 1
        # zero out pixels above threshold
        output[np.where(band > threshold)] = 0
        # if it was zero originally, we'd still like it to be zero
        output[np.where(band == 0)] = 0
        
        return output
        
    def land_to_zeros(self,threshold=50):
        """
        Take a dataset, find out which pixels in the highest numbered band have a 
        value above threshold, then set all those pixels to zero in the other 
        bands. Return an array of the modified band.
        
        :param threshold: Pixel value above which is assumed to be land.
        :type threshold: int or float
        """
        img = self.gdal_ds
        # get the highest numbered band - I'm assuming this is the longest wavelength NIR band
        nirband = img.GetRasterBand(img.RasterCount)
        nirarr = nirband.ReadAsArray()
        for bandnum in range(1,img.RasterCount + 1): # leave the nirband alone
            band = img.GetRasterBand(bandnum)
            barr = band.ReadAsArray()
            barr[np.where(nirarr > threshold)] = 0
            if bandnum==1:
                bandarr = np.array([barr])
            else:
                bandarr = np.append(bandarr,[barr],axis=0)
            # print "bandarr shape: %s" % str(bandarr.shape)
        #outfilename = output_gtif_like_img(img,bandarr,img.GetDescription().replace('.tif','_landzero.tif'))
        return bandarr
        
def output_gtif(bandarr, cols, rows, outfilename, geotransform, projection, no_data_value=-99, driver_name='GTiff', dtype=GDT_Float32):
    """Create a geotiff with gdal that will contain all the bands represented
    by arrays within bandarr which is itself array of arrays."""
    # make sure bandarr is a proper band array
    if len( bandarr.shape )==2:
        bandarr = np.array([ bandarr ])
    driver = gdal.GetDriverByName(driver_name)
    outDs = driver.Create(outfilename, cols, rows, len(bandarr), dtype)
    if outDs is None:
        print "Could not create %s" % outfilename
        sys.exit(1)
    for bandnum in range(1,len(bandarr) + 1):  # bandarr is zero based index while GetRasterBand is 1 based index
        outBand = outDs.GetRasterBand(bandnum)
        outBand.WriteArray(bandarr[bandnum - 1])
        outBand.FlushCache()
        outBand.SetNoDataValue(no_data_value)
        
    # georeference the image and set the projection
    outDs.SetGeoTransform(geotransform)
    outDs.SetProjection(projection)

    # build pyramids
    gdal.SetConfigOption('HFA_USE_RRD', 'YES')
    outDs.BuildOverviews(overviewlist=[2,4,8,16,32,64,128])
    
def output_gtif_like_img(img, bandarr, outfilename, no_data_value=-99, dtype=GDT_Float32):
    """Create a geotiff with attributes like the one passed in but make the
    values and number of bands as in bandarr."""
    cols = img.RasterXSize
    rows = img.RasterYSize
    geotransform = img.GetGeoTransform()
    projection = img.GetProjection()
    output_gtif(bandarr, cols, rows, outfilename, geotransform, projection, no_data_value, driver_name='GTiff', dtype=dtype)
    return outfilename
    
def connectivity_filter(in_array,threshold=1000,structure=None):
    """
    Take a binary array (ones and zeros), find groups of ones smaller
    than the threshold and change them to zeros.
    """
    #define how raster cells touch
    if structure:
        connection_structure = structure
    else:
        connection_structure = np.array([[0,1,0],
                                         [1,1,1],
                                         [0,1,0]])
    #perform the label operation
    labelled_array, num_features = label(in_array,structure=connection_structure)
    
    #Get the bincount for all the labels
    b_count = np.bincount(labelled_array.flat)
    
    #Then use the bincount to set the output values
    out_array = np.where(b_count[labelled_array] <= threshold, 0, in_array)
    return out_array
