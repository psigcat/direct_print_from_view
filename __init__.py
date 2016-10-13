# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DirectPrintFromView
                                 A QGIS plugin
 Print or export to a file, current map view using a composition.
                             -------------------
        begin                : 2016-10-13
        copyright            : (C) 2016 by Martí Angelats i Ribera
        email                : carlos.lopez@psig.es
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DirectPrintFromView class from file DirectPrintFromView.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .direct_print_from_view import DirectPrintFromView
    return DirectPrintFromView(iface)
