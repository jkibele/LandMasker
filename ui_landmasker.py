# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_landmasker.ui'
#
# Created: Tue May 20 16:48:42 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LandMasker(object):
    def setupUi(self, LandMasker):
        LandMasker.setObjectName(_fromUtf8("LandMasker"))
        LandMasker.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(LandMasker)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(LandMasker)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LandMasker.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LandMasker.reject)
        QtCore.QMetaObject.connectSlotsByName(LandMasker)

    def retranslateUi(self, LandMasker):
        LandMasker.setWindowTitle(QtGui.QApplication.translate("LandMasker", "LandMasker", None, QtGui.QApplication.UnicodeUTF8))

