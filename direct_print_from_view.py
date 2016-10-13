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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
import os.path
# Import the utils file
from utils import *
# Import the dialog
from ui.select_composer_dialog import Ui_SelectComposerDialog
SelectComposerDialog = Ui_SelectComposerDialog # For some reason QtDesigner or pyuic4 adds the Ui_ at the start


# Constants
EXPORT_PATH = 'export path'

# Main class
class DirectPrintFromView:
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

        # Make settings (used to save preferences)
        self.settings = QSettings("PSIG", "direct_print_from_view")

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'DirectPrintFromView_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = tr(u'&Direct Print From View')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'DirectPrintFromView')
        self.toolbar.setObjectName(u'DirectPrintFromView')


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dialog = SelectComposerDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/DirectPrintFromView/icon.png'
        self.add_action(
            icon_path,
            text=tr(u'Print view'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                tr(u'&Direct Print From View'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # Add all items (options)
        # TODO

        # Do we want to print (export otherwise)
        printAction = False

        # On print button click
        def printClicked():
            printAction = True # the only thing it actually does
            self.dialog.accept()
        # Connect function to slot
        self.dialog.ui.print_btn.clicked.connect(printClicked)

        # Show dialog
        self.dialog.show()

        # Get the dialog result
        if self.dialog.exec_():
            for result in self.dialog.ui.composer_list.selectedItems():
                centerAllCompositionMaps(composition, iface.mapCanvas().center())

                if printAction:
                    printer = askPrinter()
                    if printer is not None:
                        pass # TODO
                else:
                    # Ask where to save the exported file
                    path = QFileDialog.getSaveFileName(
                        dialog,
                        None,
                        os.path.join(
                            self.settings.value(EXPORT_PATH, os.path.expanduser("~")),      #default folder
                            refcat+"_"+dialog.ui.num_parcel_tbx.text()+".gml" #default filename
                        ),
                        "PDF (*.pdf)"
                    )

                    # If the path is not incorrect
                    if path != None and path != "":
                        # Save the folder path in the settings for the next time
                        self.settings.setValue(EXPORT_PATH, os.path.dirname(path))

                        # Finally export to PDF
                        composition.exportAsPDF(path)