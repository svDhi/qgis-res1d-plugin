# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Res1D
                                 A QGIS plugin
 This plugin load DHI res1D file in QGIS as mesh layer
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-10-14
        copyright            : (C) 2021 by Vincent Cloarec
        email                : vcloarec at gmail dot com
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



def classFactory(iface):  # pylint: disable=invalid-name
    """Load Res1D class from file Res1D.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .res1d_loader import Res1D
    return Res1D(iface)
