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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load LandMasker class from file LandMasker
    from landmasker import LandMasker
    return LandMasker(iface)
