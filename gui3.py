# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(939, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 270, 921, 221))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser.setLineWidth(4)
        self.textBrowser.setObjectName("textBrowser")
        self.combo_Selection = QtWidgets.QComboBox(self.centralwidget)
        self.combo_Selection.setGeometry(QtCore.QRect(30, 30, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_Selection.setFont(font)
        self.combo_Selection.setObjectName("combo_Selection")
        self.combo_Selection.addItem("")
        self.combo_Selection.addItem("")
        self.combo_Selection.addItem("")
        self.combo_Selection.addItem("")
        self.combo_Selection.addItem("")
        self.combo_Selection.addItem("")
        self.combo_Selection.addItem("")
        self.spinBox_nSelection = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_nSelection.setGeometry(QtCore.QRect(130, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_nSelection.setFont(font)
        self.spinBox_nSelection.setMaximum(250)
        self.spinBox_nSelection.setSingleStep(10)
        self.spinBox_nSelection.setObjectName("spinBox_nSelection")
        self.spinBox_ID = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ID.setGeometry(QtCore.QRect(30, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_ID.setFont(font)
        self.spinBox_ID.setMaximum(50)
        self.spinBox_ID.setObjectName("spinBox_ID")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 140, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 91, 20))
        self.label_3.setObjectName("label_3")
        self.spinBox_Time = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Time.setGeometry(QtCore.QRect(240, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_Time.setFont(font)
        self.spinBox_Time.setMaximum(10)
        self.spinBox_Time.setSingleStep(1)
        self.spinBox_Time.setObjectName("spinBox_Time")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 136, 91, 20))
        self.label_4.setObjectName("label_4")
        self.Save_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Save_Button.setGeometry(QtCore.QRect(950, 1000, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Save_Button.setFont(font)
        self.Save_Button.setObjectName("Save_Button")
        self.Text_Eingabe = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_Eingabe.setGeometry(QtCore.QRect(520, 70, 181, 31))
        self.Text_Eingabe.setObjectName("Text_Eingabe")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 40, 141, 20))
        self.label_5.setObjectName("label_5")
        self.combo_Selection_2 = QtWidgets.QComboBox(self.centralwidget)
        self.combo_Selection_2.setGeometry(QtCore.QRect(30, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_Selection_2.setFont(font)
        self.combo_Selection_2.setObjectName("combo_Selection_2")
        self.combo_Selection_2.addItem("")
        self.combo_Selection_2.addItem("")
        self.combo_Selection_2.addItem("")
        self.combo_Selection_2.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 70, 111, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(170, 70, 111, 16))
        self.label_7.setObjectName("label_7")
        self.combo_Selection_3 = QtWidgets.QComboBox(self.centralwidget)
        self.combo_Selection_3.setGeometry(QtCore.QRect(170, 90, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.combo_Selection_3.setFont(font)
        self.combo_Selection_3.setObjectName("combo_Selection_3")
        self.combo_Selection_3.addItem("")
        self.combo_Selection_3.addItem("")
        self.combo_Selection_3.addItem("")
        self.combo_Selection_3.addItem("")
        self.Text_Eingabe_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_Eingabe_2.setGeometry(QtCore.QRect(520, 150, 181, 31))
        self.Text_Eingabe_2.setObjectName("Text_Eingabe_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(520, 120, 141, 20))
        self.label_8.setObjectName("label_8")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(750, 150, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(750, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 860, 921, 211))
        self.graphWidget.setObjectName("graphWidget")
        self.frame_5 = QtWidgets.QFrame(self.graphWidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 921, 211))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setLineWidth(3)
        self.frame_5.setObjectName("frame_5")
        self.spinBox_Leistung_dBm = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Leistung_dBm.setGeometry(QtCore.QRect(350, 160, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_Leistung_dBm.setFont(font)
        self.spinBox_Leistung_dBm.setMaximum(33)
        self.spinBox_Leistung_dBm.setSingleStep(1)
        self.spinBox_Leistung_dBm.setObjectName("spinBox_Leistung_dBm")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 136, 111, 20))
        self.label_9.setObjectName("label_9")
        self.Clear_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Button.setGeometry(QtCore.QRect(840, 440, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Clear_Button.setFont(font)
        self.Clear_Button.setObjectName("Clear_Button")
        self.Text_Eingabe_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_Eingabe_3.setGeometry(QtCore.QRect(520, 220, 51, 31))
        self.Text_Eingabe_3.setObjectName("Text_Eingabe_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(520, 190, 61, 20))
        self.label_10.setObjectName("label_10")
        self.Text_Eingabe_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_Eingabe_4.setGeometry(QtCore.QRect(590, 220, 51, 31))
        self.Text_Eingabe_4.setObjectName("Text_Eingabe_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(590, 190, 61, 20))
        self.label_11.setObjectName("label_11")
        self.Text_Eingabe_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.Text_Eingabe_5.setGeometry(QtCore.QRect(660, 220, 51, 31))
        self.Text_Eingabe_5.setObjectName("Text_Eingabe_5")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(660, 190, 101, 16))
        self.label_12.setObjectName("label_12")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 0, 451, 261))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 16))
        self.label.setObjectName("label")
        self.Start_Button = QtWidgets.QPushButton(self.frame)
        self.Start_Button.setGeometry(QtCore.QRect(150, 210, 165, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Start_Button.setFont(font)
        self.Start_Button.setObjectName("Start_Button")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(480, 0, 451, 261))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.Plot_Button = QtWidgets.QPushButton(self.frame_2)
        self.Plot_Button.setGeometry(QtCore.QRect(270, 210, 165, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Plot_Button.setFont(font)
        self.Plot_Button.setObjectName("Plot_Button")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(480, 500, 451, 351))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(3)
        self.frame_4.setObjectName("frame_4")
        self.MplWidget_2 = MplWidget(self.frame_4)
        self.MplWidget_2.setGeometry(QtCore.QRect(0, 0, 450, 350))
        self.MplWidget_2.setObjectName("MplWidget_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 500, 451, 351))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(3)
        self.frame_3.setObjectName("frame_3")
        self.MplWidget = MplWidget(self.frame_3)
        self.MplWidget.setGeometry(QtCore.QRect(0, 0, 450, 350))
        self.MplWidget.setObjectName("MplWidget")
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.textBrowser.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.Save_Button.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.Clear_Button.raise_()
        self.Text_Eingabe.raise_()
        self.Text_Eingabe_2.raise_()
        self.Text_Eingabe_3.raise_()
        self.Text_Eingabe_4.raise_()
        self.Text_Eingabe_5.raise_()
        self.checkBox_2.raise_()
        self.checkBox.raise_()
        self.combo_Selection.raise_()
        self.combo_Selection_2.raise_()
        self.combo_Selection_3.raise_()
        self.spinBox_ID.raise_()
        self.spinBox_nSelection.raise_()
        self.spinBox_Time.raise_()
        self.spinBox_Leistung_dBm.raise_()
        self.graphWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 21))
        self.menubar.setObjectName("menubar")
        self.menuGUI_CC1110 = QtWidgets.QMenu(self.menubar)
        self.menuGUI_CC1110.setObjectName("menuGUI_CC1110")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuGUI_CC1110.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_Selection.setItemText(0, _translate("MainWindow", "Ping"))
        self.combo_Selection.setItemText(1, _translate("MainWindow", "RSSI"))
        self.combo_Selection.setItemText(2, _translate("MainWindow", "Mittelwert"))
        self.combo_Selection.setItemText(3, _translate("MainWindow", "Abstand"))
        self.combo_Selection.setItemText(4, _translate("MainWindow", "Kathrein Reader"))
        self.combo_Selection.setItemText(5, _translate("MainWindow", "Kathrein 2"))
        self.combo_Selection.setItemText(6, _translate("MainWindow", "Kathrein 2 Boards"))
        self.label_2.setText(_translate("MainWindow", "Anzahl Durchläufe"))
        self.label_3.setText(_translate("MainWindow", "ID "))
        self.label_4.setText(_translate("MainWindow", "Zeit Einstellung "))
        self.Save_Button.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "Plot Textname"))
        self.combo_Selection_2.setItemText(0, _translate("MainWindow", "SMA"))
        self.combo_Selection_2.setItemText(1, _translate("MainWindow", "Antenne 1"))
        self.combo_Selection_2.setItemText(2, _translate("MainWindow", "Monopol"))
        self.combo_Selection_2.setItemText(3, _translate("MainWindow", "Dipol"))
        self.label_6.setText(_translate("MainWindow", "Antenne Board "))
        self.label_7.setText(_translate("MainWindow", "Sende Antenne "))
        self.combo_Selection_3.setItemText(0, _translate("MainWindow", "Monopol"))
        self.combo_Selection_3.setItemText(1, _translate("MainWindow", "Dipol"))
        self.combo_Selection_3.setItemText(2, _translate("MainWindow", "Zirkular Polarisiert"))
        self.combo_Selection_3.setItemText(3, _translate("MainWindow", "Antenne 1"))
        self.label_8.setText(_translate("MainWindow", "Speichern Textname"))
        self.checkBox.setText(_translate("MainWindow", "Speichern "))
        self.checkBox_2.setText(_translate("MainWindow", "Auslesen "))
        self.label_9.setText(_translate("MainWindow", "Leistung RFID Reader in dBm"))
        self.Clear_Button.setText(_translate("MainWindow", "Clear "))
        self.label_10.setText(_translate("MainWindow", "X-Position "))
        self.label_11.setText(_translate("MainWindow", "Y-Position "))
        self.label_12.setText(_translate("MainWindow", "X-Abstand in cm"))
        self.label.setText(_translate("MainWindow", "Programm Auswahl"))
        self.Start_Button.setText(_translate("MainWindow", "Start "))
        self.Plot_Button.setText(_translate("MainWindow", "Plot Graph"))
        self.menuGUI_CC1110.setTitle(_translate("MainWindow", "GUI CC1110"))
from mplwidget import MplWidget
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
