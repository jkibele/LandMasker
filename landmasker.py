# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LandMasker
                                 A QGIS plugin
 Generate a mask from a multispectral image to separate land from water.
                              -------------------
        begin                : 2014-05-14
        copyright            : (C) 2014 by Jared Kibele
        email                : jkibele@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from landmaskerdialog import LandMaskerDialog
import os.path

#- Add my imports
from raster_handling import *


class LandMasker:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'landmasker_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = LandMaskerDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/landmasker/icon.png"),
            u"Multispec Land Mask", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Multispectral Land Mask", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Multispectral Land Mask", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work    
    def run(self):
        #- populate the combo box with loaded layers
        self.dlg.initLayerCombobox( self.dlg.inputRasterComboBox, 'key_of_default_layer' )
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            #- get the  layer
            rast_layer = self.dlg.layerFromComboBox( self.dlg.inputRasterComboBox )
            rds = RasterDS( rast_layer )
            # get the filename
            filename = str( self.dlg.outputRasterLineEdit.text() )
            # get the threshold from the dialog
            thresh = float( self.dlg.thresholdDoubleSpinBox.text() )
            # get connectivity threshold
            connthresh = int( self.dlg.connectivitySpinBox.text() )
            #mask_band = rds.ward_cluster_land_mask()
            simple_mask = rds.simple_land_mask(threshold=thresh)
            
            # filter out small patches
            mask_band = connectivity_filter(simple_mask,threshold=connthresh)
            
            outfile = rds.new_image_from_array(mask_band,outfilename=filename)
            
            if self.dlg.addMaskCheckBox.isChecked():
                fileInfo = QFileInfo(filename)
                baseName = fileInfo.baseName()
                rlayer = QgsRasterLayer(filename, baseName)
                if not rlayer.isValid():
                    #print "Layer failed to load!"
                    mbox = QMessageBox()
                    outtext = "Layer failed to load!"
                    mbox.setText( outtext )
                    mbox.setWindowTitle( "Error" )
                    mbox.exec_()
                QgsMapLayerRegistry.instance().addMapLayer(rlayer)
