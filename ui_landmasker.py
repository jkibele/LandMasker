# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_landmasker.ui'
#
# Created: Fri May 16 11:39:37 2014
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
        LandMasker.resize(388, 352)
        self.verticalLayout_4 = QtGui.QVBoxLayout(LandMasker)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.inputRasterGroupBox = QtGui.QGroupBox(LandMasker)
        self.inputRasterGroupBox.setObjectName(_fromUtf8("inputRasterGroupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.inputRasterGroupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.inputRasterComboBox = QtGui.QComboBox(self.inputRasterGroupBox)
        self.inputRasterComboBox.setObjectName(_fromUtf8("inputRasterComboBox"))
        self.verticalLayout_3.addWidget(self.inputRasterComboBox)
        self.verticalLayout_4.addWidget(self.inputRasterGroupBox)
        spacerItem = QtGui.QSpacerItem(156, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.groupBox = QtGui.QGroupBox(LandMasker)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.thresholdDoubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.thresholdDoubleSpinBox.setMaximum(9999.99)
        self.thresholdDoubleSpinBox.setProperty("value", 50.0)
        self.thresholdDoubleSpinBox.setObjectName(_fromUtf8("thresholdDoubleSpinBox"))
        self.horizontalLayout_3.addWidget(self.thresholdDoubleSpinBox)
        self.thresholdLabel = QtGui.QLabel(self.groupBox)
        self.thresholdLabel.setObjectName(_fromUtf8("thresholdLabel"))
        self.horizontalLayout_3.addWidget(self.thresholdLabel)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.connectivitySpinBox = QtGui.QSpinBox(self.groupBox)
        self.connectivitySpinBox.setMaximum(99999)
        self.connectivitySpinBox.setSingleStep(10)
        self.connectivitySpinBox.setProperty("value", 1000)
        self.connectivitySpinBox.setObjectName(_fromUtf8("connectivitySpinBox"))
        self.horizontalLayout_2.addWidget(self.connectivitySpinBox)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addWidget(self.groupBox)
        spacerItem3 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.outputRasterGroupBox = QtGui.QGroupBox(LandMasker)
        self.outputRasterGroupBox.setObjectName(_fromUtf8("outputRasterGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.outputRasterGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.outputRasterLineEdit = QtGui.QLineEdit(self.outputRasterGroupBox)
        self.outputRasterLineEdit.setObjectName(_fromUtf8("outputRasterLineEdit"))
        self.horizontalLayout.addWidget(self.outputRasterLineEdit)
        self.selectPushButton = QtGui.QPushButton(self.outputRasterGroupBox)
        self.selectPushButton.setObjectName(_fromUtf8("selectPushButton"))
        self.horizontalLayout.addWidget(self.selectPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.addMaskCheckBox = QtGui.QCheckBox(self.outputRasterGroupBox)
        self.addMaskCheckBox.setChecked(True)
        self.addMaskCheckBox.setObjectName(_fromUtf8("addMaskCheckBox"))
        self.verticalLayout_2.addWidget(self.addMaskCheckBox)
        self.verticalLayout_4.addWidget(self.outputRasterGroupBox)
        self.buttonBox = QtGui.QDialogButtonBox(LandMasker)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(LandMasker)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), LandMasker.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), LandMasker.reject)
        QtCore.QObject.connect(self.selectPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), LandMasker.showFileSelectDialog)
        QtCore.QMetaObject.connectSlotsByName(LandMasker)
        LandMasker.setTabOrder(self.inputRasterComboBox, self.outputRasterLineEdit)
        LandMasker.setTabOrder(self.outputRasterLineEdit, self.selectPushButton)
        LandMasker.setTabOrder(self.selectPushButton, self.addMaskCheckBox)
        LandMasker.setTabOrder(self.addMaskCheckBox, self.buttonBox)

    def retranslateUi(self, LandMasker):
        LandMasker.setWindowTitle(QtGui.QApplication.translate("LandMasker", "LandMask", None, QtGui.QApplication.UnicodeUTF8))
        self.inputRasterGroupBox.setTitle(QtGui.QApplication.translate("LandMasker", "Input Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("LandMasker", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdDoubleSpinBox.setToolTip(QtGui.QApplication.translate("LandMasker", "<html><head/><body><p>Pixel value below which that pixel will be considered as water. The default value is reasonable for near infrared bands in units of raw digital numbers. If the image units are different, you\'ll have to inspect the image and pick an appropriate value.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.thresholdLabel.setText(QtGui.QApplication.translate("LandMasker", "Value Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.connectivitySpinBox.setToolTip(QtGui.QApplication.translate("LandMasker", "<html><head/><body><p>Pixels below the value threshold must be part of a group of this many contiguous pixels in order to be considered water. The intention is to eliminate shadow areas on land.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LandMasker", "Connectivity Threshold", None, QtGui.QApplication.UnicodeUTF8))
        self.outputRasterGroupBox.setTitle(QtGui.QApplication.translate("LandMasker", "Output Raster", None, QtGui.QApplication.UnicodeUTF8))
        self.selectPushButton.setText(QtGui.QApplication.translate("LandMasker", "Select...", None, QtGui.QApplication.UnicodeUTF8))
        self.addMaskCheckBox.setText(QtGui.QApplication.translate("LandMasker", "Add Mask to Project", None, QtGui.QApplication.UnicodeUTF8))

