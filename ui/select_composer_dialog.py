# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_composer_dialog.ui'
#
# Created: Thu Oct 13 19:06:52 2016
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SelectComposerDialog(object):
    def setupUi(self, SelectComposerDialog):
        SelectComposerDialog.setObjectName(_fromUtf8("SelectComposerDialog"))
        SelectComposerDialog.resize(401, 370)
        self.verticalLayout = QtGui.QVBoxLayout(SelectComposerDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.composer_list = QtGui.QListWidget(SelectComposerDialog)
        self.composer_list.setObjectName(_fromUtf8("composer_list"))
        self.verticalLayout.addWidget(self.composer_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.print_btn = QtGui.QPushButton(SelectComposerDialog)
        self.print_btn.setObjectName(_fromUtf8("print_btn"))
        self.horizontalLayout.addWidget(self.print_btn)
        self.export_btn = QtGui.QPushButton(SelectComposerDialog)
        self.export_btn.setObjectName(_fromUtf8("export_btn"))
        self.horizontalLayout.addWidget(self.export_btn)
        self.cancel_btn = QtGui.QPushButton(SelectComposerDialog)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SelectComposerDialog)
        QtCore.QMetaObject.connectSlotsByName(SelectComposerDialog)
        SelectComposerDialog.setTabOrder(self.cancel_btn, self.composer_list)
        SelectComposerDialog.setTabOrder(self.composer_list, self.export_btn)
        SelectComposerDialog.setTabOrder(self.export_btn, self.print_btn)

    def retranslateUi(self, SelectComposerDialog):
        SelectComposerDialog.setWindowTitle(_translate("SelectComposerDialog", "Select Composer", None))
        self.print_btn.setText(_translate("SelectComposerDialog", "Print", None))
        self.export_btn.setText(_translate("SelectComposerDialog", "Export to PDF", None))
        self.cancel_btn.setText(_translate("SelectComposerDialog", "Cancel", None))

