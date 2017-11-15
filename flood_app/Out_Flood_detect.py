# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Flood_detect.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import arcpy
import data_process as dp

class Ui_Dialog(QtWidgets.QWidget):

    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(965, 746)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(180, 720, 611, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(60, 320, 411, 301))
        self.groupBox.setObjectName("groupBox")
        self.comboBox_defaultThreshold = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_defaultThreshold.setGeometry(QtCore.QRect(20, 70, 351, 22))
        self.comboBox_defaultThreshold.setObjectName("comboBox_defaultThreshold")
        self.comboBox_defaultThreshold.addItem("")
        self.comboBox_defaultThreshold.addItem("")
        self.checkBox_defaultThreshold = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_defaultThreshold.setGeometry(QtCore.QRect(20, 40, 111, 20))
        self.checkBox_defaultThreshold.setObjectName("checkBox_defaultThreshold")
        self.checkBox_defineThreshold = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_defineThreshold.setGeometry(QtCore.QRect(20, 150, 121, 20))
        self.checkBox_defineThreshold.setObjectName("checkBox_defineThreshold")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 190, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 81, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_defineDeltaNDWI = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_defineDeltaNDWI.setGeometry(QtCore.QRect(120, 190, 104, 21))
        self.textEdit_defineDeltaNDWI.setObjectName("textEdit_defineDeltaNDWI")
        self.textEdit_definePostNDWI = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_definePostNDWI.setGeometry(QtCore.QRect(120, 230, 104, 21))
        self.textEdit_definePostNDWI.setObjectName("textEdit_definePostNDWI")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(520, 320, 411, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 50, 101, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_maskType = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_maskType.setGeometry(QtCore.QRect(30, 80, 191, 22))
        self.comboBox_maskType.setObjectName("comboBox_maskType")
        self.comboBox_maskType.addItem("")
        self.comboBox_maskType.addItem("")
        self.comboBox_maskType.addItem("")
        self.comboBox_maskType.addItem("")
        self.comboBox_maskType.addItem("")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 101, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_confidence = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_confidence.setGeometry(QtCore.QRect(30, 180, 191, 22))
        self.comboBox_confidence.setObjectName("comboBox_confidence")
        self.comboBox_confidence.addItem("")
        self.comboBox_confidence.addItem("")
        self.comboBox_confidence.addItem("")
        self.comboBox_confidence.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(130, 20, 701, 291))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_preFlood = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_preFlood.setGeometry(QtCore.QRect(400, 40, 93, 28))
        self.pushButton_preFlood.setObjectName("pushButton_preFlood")
        self.pushButton_postFlood = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_postFlood.setGeometry(QtCore.QRect(400, 100, 93, 28))
        self.pushButton_postFlood.setObjectName("pushButton_postFlood")
        self.textEdit_3 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_3.setGeometry(QtCore.QRect(-200, 230, 104, 87))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_preFlood = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_preFlood.setGeometry(QtCore.QRect(0, 40, 401, 31))
        self.textEdit_preFlood.setObjectName("textEdit_preFlood")
        self.textEdit_postFlood = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_postFlood.setGeometry(QtCore.QRect(0, 100, 401, 31))
        self.textEdit_postFlood.setObjectName("textEdit_postFlood")
        self.textEdit_outputProcess = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_outputProcess.setGeometry(QtCore.QRect(0, 220, 401, 31))
        self.textEdit_outputProcess.setObjectName("textEdit_outputProcess")
        self.comboBox_landsatType = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_landsatType.setGeometry(QtCore.QRect(540, 60, 111, 22))
        self.comboBox_landsatType.setObjectName("comboBox_landsatType")
        self.comboBox_landsatType.addItem("")
        self.comboBox_landsatType.addItem("")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(560, 30, 71, 16))
        self.label_5.setObjectName("label_5")
        self.textEdit_shapefile = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_shapefile.setGeometry(QtCore.QRect(0, 160, 401, 31))
        self.textEdit_shapefile.setObjectName("textEdit_shapefile")
        self.pushButton_shapefile = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_shapefile.setGeometry(QtCore.QRect(400, 160, 93, 28))
        self.pushButton_shapefile.setObjectName("pushButton_shapefile")
        self.pushButton_OK = QtWidgets.QPushButton(Dialog)
        self.pushButton_OK.setGeometry(QtCore.QRect(380, 660, 93, 28))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.pushButton_Cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(520, 660, 93, 28))
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.progressBar.raise_()
        self.pushButton_OK.raise_()
        self.pushButton_Cancel.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.comboBox_defaultThreshold.setEnabled (False)
        self.textEdit_defineDeltaNDWI.setEnabled (False)
        self.textEdit_definePostNDWI.setEnabled (False)

        self.checkBox_defaultThreshold.toggled.connect(self.checkbox_toggled)
        self.checkBox_defineThreshold.toggled.connect(self.checkbox_toggled)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Threshold"))
        self.comboBox_defaultThreshold.setItemText(0, _translate("Dialog", "Gao(deltaNDWI >= 0.094 ; duringNDWI >= 0.161)"))
        self.comboBox_defaultThreshold.setItemText(1, _translate("Dialog", "McFeeters(deltaNDWI >= 0.228 ; duringNDWI >= 0.548)"))
        self.checkBox_defaultThreshold.setText(_translate("Dialog", "Default source"))
        self.checkBox_defineThreshold.setText(_translate("Dialog", "Define yourself"))
        self.label.setText(_translate("Dialog", "Delta NDWI"))
        self.label_2.setText(_translate("Dialog", "NDWI during"))
        self.groupBox_2.setTitle(_translate("Dialog", "Cloud Mask"))
        self.label_3.setText(_translate("Dialog", "Mask Type"))
        self.comboBox_maskType.setItemText(0, _translate("Dialog", "Cloud"))
        self.comboBox_maskType.setItemText(1, _translate("Dialog", "Cirrus"))
        self.comboBox_maskType.setItemText(2, _translate("Dialog", "Snow"))
        self.comboBox_maskType.setItemText(3, _translate("Dialog", "Vegetation"))
        self.comboBox_maskType.setItemText(4, _translate("Dialog", "Water"))
        self.label_4.setText(_translate("Dialog", "Confidence"))
        self.comboBox_confidence.setItemText(0, _translate("Dialog", "High"))
        self.comboBox_confidence.setItemText(1, _translate("Dialog", "Medium"))
        self.comboBox_confidence.setItemText(2, _translate("Dialog", "Low"))
        self.comboBox_confidence.setItemText(3, _translate("Dialog", "None"))
        self.groupBox_3.setTitle(_translate("Dialog", "Data directory"))
        self.pushButton_preFlood.setText(_translate("Dialog", "Browse"))
        self.pushButton_postFlood.setText(_translate("Dialog", "Browse"))
        self.textEdit_preFlood.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">directoryPreFlood</p></body></html>"))
        self.textEdit_postFlood.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">directoryPostFlood</p></body></html>"))
        self.textEdit_outputProcess.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">outputDirectory</p></body></html>"))
        self.comboBox_landsatType.setItemText(0, _translate("Dialog", "Landsat8"))
        self.comboBox_landsatType.setItemText(1, _translate("Dialog", "Landsat7"))
        self.label_5.setText(_translate("Dialog", "Jenis Data"))
        self.textEdit_shapefile.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">projectedShapefile</p></body></html>"))
        self.pushButton_shapefile.setText(_translate("Dialog", "Browse"))
        self.pushButton_OK.setText(_translate("Dialog", "OK"))
        self.pushButton_Cancel.setText(_translate("Dialog", "Cancel"))

        self.pushButton_preFlood.clicked.connect(self.openPreFlood)
        self.pushButton_postFlood.clicked.connect(self.openPostFlood)
        self.pushButton_shapefile.clicked.connect(self.openShapeFile)
        self.pushButton_OK.clicked.connect(self.executeCode)

    def checkbox_toggled(self):
        if (self.checkBox_defaultThreshold.isChecked() == True):
            self.checkBox_defineThreshold.setEnabled (False)
            self.comboBox_defaultThreshold.setEnabled (True)

        else:
            self.checkBox_defineThreshold.setEnabled (True)
            self.comboBox_defaultThreshold.setEnabled (False)

        if (self.checkBox_defineThreshold.isChecked() == True):
            self.checkBox_defaultThreshold.setEnabled (False)
            self.textEdit_defineDeltaNDWI.setEnabled (True)
            self.textEdit_definePostNDWI.setEnabled (True)

        else:
            self.checkBox_defaultThreshold.setEnabled (True)
            self.textEdit_defineDeltaNDWI.setEnabled (False)
            self.textEdit_definePostNDWI.setEnabled (False)


    def openPreFlood(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.textEdit_preFlood.setText(fileName)
        self.textEdit_outputProcess.setText(fileName+'_OutputTools')
        #print(fileName)

    def openPostFlood(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')
        self.textEdit_postFlood.setText(fileName)
        #print(fileName)

    def openShapeFile(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        self.textEdit_shapefile.setText(fileName)
        #print(fileName)


    def executeCode(self):
        data_type = self.comboBox_landsatType.currentText()

        pre_flood = self.textEdit_preFlood.toPlainText()
        post_flood = self.textEdit_postFlood.toPlainText()
        out_process = self.textEdit_outputProcess.toPlainText()
        inFC = self.textEdit_shapefile.toPlainText()
        

        print(pre_flood)
        print(post_flood)
        print(out_process)

        if(self.checkBox_defaultThreshold.isChecked() == True):

            print("Default Threshold")
            if(self.comboBox_defaultThreshold.currentText() == "Gao"):
                print("Gao")
                deltaNDWI = "0.094"
                NDWIduring = "0.161"
            else:
                print("McFeeter")
                deltaNDWI = "0.228"
                NDWIduring = "0.548"
        else:

            print("Define Threshold")
            deltaNDWI = self.textEdit_defineDeltaNDWI.toPlainText()
            NDWIduring = self.textEdit_definePostNDWI.toPlainText()
            print(deltaNDWI)
            print(NDWIduring)

        masktype = self.comboBox_maskType.currentText()
        confidence = self.comboBox_confidence.currentText()
        cummulative = 'false'

        print(masktype)
        print(confidence)

        os.mkdir(out_process)
        dp.mask_cloud(pre_flood, masktype, confidence, cummulative, out_process)
        dp.mask_cloud(post_flood, masktype, confidence, cummulative, out_process)
        # dp.process_landsat(pre_flood, arcpy.Describe(inFC).spatialReference, out_process, "_PreFlood", data_type)
        # dp.process_landsat(post_flood, arcpy.Describe(inFC).spatialReference, out_process, "_PostFlood", data_type)
        # dp.diffNDWI(out_process, os.path.basename(pre_flood), os.path.basename(post_flood))
        # dp.pixelExtraction(out_process, os.path.basename(pre_flood), os.path.basename(post_flood))

        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())

