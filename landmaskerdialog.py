# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LandMaskerDialog
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

from PyQt4 import QtCore, QtGui
from ui_landmasker import Ui_LandMasker
# create the dialog for zoom to point

# next imports added manually:
import os
from qgis.core import QgsMapLayerRegistry, QgsMapLayer

class LandMaskerDialog(QtGui.QDialog, Ui_LandMasker):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    #- everything below added manually:
    def initLayerCombobox(self,combobox, default):
         combobox.clear()
         reg = QgsMapLayerRegistry.instance()
         for ( key, layer ) in reg.mapLayers().iteritems():
             
             if layer.type() == QgsMapLayer.RasterLayer and ( layer.dataProvider().name() == 'gdal' ):
                 combobox.addItem( layer.name(), key )
         
         idx = combobox.findData( default )
         if idx != -1:
             combobox.setCurrentIndex( idx ) 
             
    def layerFromComboBox(self, combobox):
        layerID = combobox.itemData(combobox.currentIndex())
        return QgsMapLayerRegistry.instance().mapLayer( layerID )
        
    def showFileSelectDialog(self):
        fname = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.path.expanduser('~'))
        self.outputRasterLineEdit.setText( fname )