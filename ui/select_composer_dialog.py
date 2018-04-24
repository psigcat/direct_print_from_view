# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_composer_dialog.ui'
#
# Created: Fri Oct 14 12:21:28 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!
from builtins import object
from qgis.PyQt import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
#from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_SelectComposerDialog(object):
    def setupUi(self, SelectComposerDialog):
        SelectComposerDialog.setObjectName(_fromUtf8("SelectComposerDialog"))
        SelectComposerDialog.resize(401, 370)
        self.verticalLayout = QtWidgets.QVBoxLayout(SelectComposerDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.composer_list = QtWidgets.QListWidget(SelectComposerDialog)
        self.composer_list.setObjectName(_fromUtf8("composer_list"))
        self.verticalLayout.addWidget(self.composer_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.print_btn = QtWidgets.QPushButton(SelectComposerDialog)
        self.print_btn.setObjectName(_fromUtf8("print_btn"))
        self.horizontalLayout.addWidget(self.print_btn)
        self.export_btn = QtWidgets.QPushButton(SelectComposerDialog)
        self.export_btn.setObjectName(_fromUtf8("export_btn"))
        self.horizontalLayout.addWidget(self.export_btn)
        self.cancel_btn = QtWidgets.QPushButton(SelectComposerDialog)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SelectComposerDialog)
        #QtCore.QObject.connect(self.export_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), SelectComposerDialog.accept)
        self.export_btn.clicked.connect(SelectComposerDialog.accept)
        #QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), SelectComposerDialog.reject)
        self.cancel_btn.clicked.connect(SelectComposerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SelectComposerDialog)
        SelectComposerDialog.setTabOrder(self.cancel_btn, self.composer_list)
        SelectComposerDialog.setTabOrder(self.composer_list, self.export_btn)
        SelectComposerDialog.setTabOrder(self.export_btn, self.print_btn)

    def retranslateUi(self, SelectComposerDialog):
        SelectComposerDialog.setWindowTitle(_translate("SelectComposerDialog", "Select Composer", None))
        self.print_btn.setText(_translate("SelectComposerDialog", "Print", None))
        self.export_btn.setText(_translate("SelectComposerDialog", "Export to PDF", None))
        self.cancel_btn.setText(_translate("SelectComposerDialog", "Cancel", None))

