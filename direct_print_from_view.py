# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DirectPrintFromView
                                 A QGIS plugin
 Print or export to a file, current map view using a composition.
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
from __future__ import absolute_import
from builtins import object
from qgis.PyQt.QtCore import Qt, QSettings, QTranslator, qVersion, QCoreApplication
from qgis.PyQt.QtWidgets import QAction, QDialog, QFileDialog, QListWidget,QMessageBox
from qgis.PyQt.QtGui import QIcon
from qgis.core import QgsProject,QgsLayoutExporter
import os.path
import datetime
# Import the utils file
from .utils import openFile,centerAllCompositionMaps,centerRect,askPrinter,tr
# Import the dialog
from .ui.select_composer_dialog import Ui_SelectComposerDialog


# Constants
EXPORT_PATH = 'export path'

# Main class
class DirectPrintFromView(object):
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # Safe plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        self.icon = QIcon(os.path.join(self.plugin_dir, 'icon.png'))

        # Make settings (used to save preferences)
        self.settings = QSettings("PSIG", "direct_print_from_view")

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'direct_print_from_view_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.dialog = QDialog(None, Qt.WindowSystemMenuHint | Qt.WindowTitleHint)
        self.dialog.ui = Ui_SelectComposerDialog()
        self.dialog.ui.setupUi(self.dialog)
        self.dialog.setWindowIcon(self.icon)

        self.action = QAction(self.icon, tr("Print View"), self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(tr("Direct Print From View"), self.action)



    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        self.iface.removePluginMenu(tr("Direct Print From View"), self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        """Run method that performs all the real work"""
        # If there is no project open
        if not QgsProject.instance().title():
            return

        # Clear list (remove all elements)
        self.dialog.ui.composer_list.clear()
        # Add all items (options)
        projectInstance=QgsProject.instance()
        
        composers=projectInstance.layoutManager()

        for c in composers.printLayouts():
            self.dialog.ui.composer_list.addItem(c.name())

        # Do we want to print? (export otherwise. False by default)
        self.printAction = False

        # Connect function to slot
        self.dialog.ui.print_btn.clicked.connect(self.printClicked)

        # Show dialog
        self.dialog.show()

        # Get the dialog result
        if self.dialog.exec_():
            # Aquire the desired composition
            
            composition = composers.layouts()[self.dialog.ui.composer_list.currentRow()] #selected composer in the widjet
            centerAllCompositionMaps(composition, self.iface.mapCanvas().center())
            composer=QgsLayoutExporter(composition)

            # Print or export
            if self.printAction:
                # Get the printer
                printer = askPrinter(self.icon)
                # Make sure it actually selected a printer
                if printer is not None:
                    success = composer.print(printer, QgsLayoutExporter.PrintExportSettings())
                    if success != 0:
                        QMessageBox.warning(self.iface.mainWindow(), self.tr("Print Failed"), self.tr("Failed to print the layout."))
                    
            else:
                # Ask where to save the exported file

                path, __ = QFileDialog.getSaveFileName(
                    None,
                    None,
                    os.path.join(
                        self.settings.value(EXPORT_PATH, os.path.expanduser("~")),      #default folder
                        ""
                    ),
                    "PDF (*.pdf)"
                )

                # If the path is not incorrect
                if path != None and path != "":
                    # Save the folder path in the settings for the next time
                    self.settings.setValue(EXPORT_PATH, os.path.dirname(path))

                    # Export to PDF
                    composer.exportToPdf(path,QgsLayoutExporter.PdfExportSettings() )
                    # And show the result using the default application
                    openFile(path)


    # On print button click
    def printClicked(self):
        """Function which is called when the print button of the dialog is pressed."""
        self.printAction = True # the only thing it actually does
        self.dialog.accept()