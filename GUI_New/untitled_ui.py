# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ADMIN\Desktop\งาน มจพ\ปี 4 เทอม 2\software\tw\GUINew\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1044, 692)
        MainWindow.setStyleSheet("background-color: rgb(41, 70, 91);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 210, 91, 31))
        self.pushButton_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(40, 340, 251, 261))
        self.tableView.setObjectName("tableView")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 270, 271, 23))
        self.progressBar.setStyleSheet("color:rgb(87, 95, 255);\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(220, 60, 121, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(220, 100, 121, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(290, 150, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(370, 30, 331, 271))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(890, 350, 121, 61))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(720, 30, 311, 271))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, -20, 191, 81))
        self.label.setStyleSheet("color:rgb(29, 161, 242);\n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 50, 141, 121))
        self.frame.setStyleSheet("border-image: url(:/image/Twitter-logo.svg.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(370, 350, 461, 271))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 191, 31))
        self.lineEdit.setStyleSheet("color:rgb(255, 255, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 310, 191, 20))
        self.label_2.setStyleSheet("color:rgb(29, 161, 242);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 0, 191, 20))
        self.label_3.setStyleSheet("color:rgb(29, 161, 242);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 320, 191, 20))
        self.label_4.setStyleSheet("color:rgb(29, 161, 242);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 0, 191, 20))
        self.label_5.setStyleSheet("color:rgb(29, 161, 242);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(210, 150, 61, 20))
        self.label_6.setStyleSheet("color:rgb(29, 161, 242);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(890, 420, 121, 201))
        self.graphicsView_5.setObjectName("graphicsView_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1044, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Twitter NLP"))
        self.lineEdit.setText(_translate("MainWindow", "   Enter your word"))
        self.label_2.setText(_translate("MainWindow", "Raw Data"))
        self.label_3.setText(_translate("MainWindow", "Top 10 Rank"))
        self.label_4.setText(_translate("MainWindow", "Map"))
        self.label_5.setText(_translate("MainWindow", "Sentiment"))
        self.label_6.setText(_translate("MainWindow", "Language"))
import Myimage_rc
