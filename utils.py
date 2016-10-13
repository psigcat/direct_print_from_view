# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Utilities of DirectPrintFromView
                              -------------------
        begin                : 2016-10-13
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Martí Angelats i Ribera
        email                : carlos.lopez@psig.es
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

def centerAllCompositionMaps(composition, center):
	"""Centers any map in the composition to the required center without changing the scale.

	:param composition: Composition to center the maps from.
	:type composition: QgsComposer

	:param center: Where to center the maps to.
	:type center: QgsPoint
	"""

	# Iterate all items of the composition
	for item in composition.items():
		# Only use the maps
		if isinstance(item, QgsComposerMap):
			# Center the view to center (without changing the scale)
			item.setNewExtent(centerRect(item.extent(), center))


def centerRect(rect, center):
	"""Makes a new rectangle which is the translation of 'rect' where its center is 'center'.

	:param rect: Original rectangle.
	:type rect: QgsRectangle

	:param center: The center of the translated rectangle.
	:type center: QgsPoint
	"""
	# Half the width and haf the height. Used later
	hw = rect.width() / 2
	hh = rect.height() / 2

	# Calculate the minimum point
	xMin = center.x() - hw
	yMin = center.y() - hh

	# Calculate the maximum point
	xMax = center.x() + hw
	yMax = center.y() + hh

	# Make and return the new rectangle (we don't really care about the actual type)
	return type(rect)(xMin, yMin, xMax, yMax)


def askPrinter():
	"""Returns a new object representing the selected printer. None if canceled."""

	# Show dialog
	printer = QPrinter()
	select = QPrintDialog(printer)

	# Return the result. None if canceled
	if select.exec_():
		return printer
	else:
		return None


def tr(text):
	"""Translates the text using QtTranslator.

	:param text: Text to be translated.
	:type text: str or unicode
	"""
	return QApplication.translate("ficha_urbanistica", text)