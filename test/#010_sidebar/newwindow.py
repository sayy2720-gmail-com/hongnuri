
from PyQt5 import QtCore, QtGui, QtWidgets
##
from newwindow1 import Ui_newwindow11
import subprocess


class Ui_NewWindow1(object):
    def openwindow(self, index):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newwindow11()
        self.ui.setupUi(self.window)
        self.window.show()
        ## 페이지 번호지정
        self.ui.stackedWidget.setCurrentIndex(index)
    def setupUi(self, NewWindow1):
        NewWindow1.setObjectName("NewWindow1")
        NewWindow1.resize(546, 811)
        NewWindow1.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(NewWindow1)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 531, 811))
        self.stackedWidget.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_2 = QtWidgets.QLabel(self.page_1)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.splitter_2 = QtWidgets.QSplitter(self.page_1)
        self.splitter_2.setGeometry(QtCore.QRect(20, 70, 501, 711))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.chapter1_1 = QtWidgets.QPushButton(self.splitter_2, clicked=lambda: self.openwindow(0))
        self.chapter1_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 103, 52);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter1_1.setObjectName("chapter1_1")
        self.chapter1_2 = QtWidgets.QPushButton(self.splitter_2, clicked=lambda: self.openwindow(4))
        self.chapter1_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 103, 52);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter1_2.setObjectName("chapter1_2")
        self.chapter1_3 = QtWidgets.QPushButton(self.splitter_2, clicked=lambda: self.openwindow(7))
        self.chapter1_3.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 103, 52);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter1_3.setObjectName("chapter1_3")
        self.chapter1_4 = QtWidgets.QPushButton(self.splitter_2, clicked=lambda: self.openwindow(11))
        self.chapter1_4.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 103, 52);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter1_4.setObjectName("chapter1_4")
        self.chapter1_test = QtWidgets.QPushButton(self.splitter_2, clicked=self.run_2py)
        self.chapter1_test.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter1_test.setObjectName("chapter1_test")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label2 = QtWidgets.QLabel(self.page_2)
        self.label2.setGeometry(QtCore.QRect(170, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.splitter = QtWidgets.QSplitter(self.page_2)
        self.splitter.setGeometry(QtCore.QRect(10, 100, 511, 661))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.chapter2_1 = QtWidgets.QPushButton(self.splitter, clicked=lambda: self.openwindow(15))
        self.chapter2_1.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 103, 52);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter2_1.setObjectName("chapter2_1")
        self.chapter2_2 = QtWidgets.QPushButton(self.splitter, clicked=lambda: self.openwindow(22))
        self.chapter2_2.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 103, 52);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter2_2.setObjectName("chapter2_2")
        self.chapter2_test = QtWidgets.QPushButton(self.splitter, clicked=lambda: self.openwindow(29))
        self.chapter2_test.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter2_test.setObjectName("chapter2_test")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label3 = QtWidgets.QLabel(self.page_3)
        self.label3.setGeometry(QtCore.QRect(180, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.splitter_4 = QtWidgets.QSplitter(self.page_3)
        self.splitter_4.setGeometry(QtCore.QRect(30, 70, 471, 701))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.chapter3_1 = QtWidgets.QPushButton(self.splitter_4, clicked=lambda: self.openwindow(39))
        self.chapter3_1.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 173, 90);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter3_1.setObjectName("chapter3_1")
        self.chapter3_test = QtWidgets.QPushButton(self.splitter_4, clicked=lambda: self.openwindow(29))
        self.chapter3_test.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter3_test.setObjectName("chapter3_test")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label4 = QtWidgets.QLabel(self.page_4)
        self.label4.setGeometry(QtCore.QRect(180, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.splitter_5 = QtWidgets.QSplitter(self.page_4)
        self.splitter_5.setGeometry(QtCore.QRect(20, 75, 491, 691))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.chapter4_1 = QtWidgets.QPushButton(self.splitter_5, clicked=lambda: self.openwindow(47))
        self.chapter4_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 173, 90);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter4_1.setObjectName("chapter4_1")
        self.chapter4_2 = QtWidgets.QPushButton(self.splitter_5, clicked=lambda: self.openwindow(55))
        self.chapter4_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 173, 90);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter4_2.setObjectName("chapter4_2")
        self.chapter4_3 = QtWidgets.QPushButton(self.splitter_5, clicked=lambda: self.openwindow(60))
        self.chapter4_3.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 173, 90);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter4_3.setObjectName("chapter4_3")
        self.chapter4_4 = QtWidgets.QPushButton(self.splitter_5, clicked=lambda: self.openwindow(65))
        self.chapter4_4.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 173, 90);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter4_4.setObjectName("chapter4_4")
        self.chapter4_5 = QtWidgets.QPushButton(self.splitter_5, clicked=lambda: self.openwindow(69))
        self.chapter4_5.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"    background-color: rgb(255, 173, 90);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter4_5.setObjectName("chapter4_5")
        self.chapter4_test = QtWidgets.QPushButton(self.splitter_5, clicked=lambda: self.openwindow(29))
        self.chapter4_test.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter4_test.setObjectName("chapter4_test")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label5 = QtWidgets.QLabel(self.page_5)
        self.label5.setGeometry(QtCore.QRect(170, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.splitter_6 = QtWidgets.QSplitter(self.page_5)
        self.splitter_6.setGeometry(QtCore.QRect(10, 70, 511, 711))
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.chapter5_1 = QtWidgets.QPushButton(self.splitter_6, clicked=lambda: self.openwindow(83))
        self.chapter5_1.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(56, 56, 56);\n"
"    background-color: rgb(255, 234, 5);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter5_1.setObjectName("chapter5_1")
        self.chapter5_test = QtWidgets.QPushButton(self.splitter_6, clicked=lambda: self.openwindow(29))
        self.chapter5_test.setStyleSheet("QPushButton{\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter5_test.setObjectName("chapter5_test")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label6 = QtWidgets.QLabel(self.page_6)
        self.label6.setGeometry(QtCore.QRect(180, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.splitter_7 = QtWidgets.QSplitter(self.page_6)
        self.splitter_7.setGeometry(QtCore.QRect(10, 70, 511, 711))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.chapter6_1 = QtWidgets.QPushButton(self.splitter_7, clicked=lambda: self.openwindow(91))
        self.chapter6_1.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(56, 56, 56);\n"
"    background-color: rgb(255, 234, 5);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter6_1.setObjectName("chapter6_1")
        self.chapter6_2 = QtWidgets.QPushButton(self.splitter_7, clicked=lambda: self.openwindow(99))
        self.chapter6_2.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(56, 56, 56);\n"
"    background-color: rgb(255, 234, 5);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter6_2.setObjectName("chapter6_2")
        self.chapter6_3 = QtWidgets.QPushButton(self.splitter_7, clicked=lambda: self.openwindow(104))
        self.chapter6_3.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(56, 56, 56);\n"
"    background-color: rgb(255, 234, 5);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter6_3.setObjectName("chapter6_3")
        self.chapter6_test = QtWidgets.QPushButton(self.splitter_7, clicked=lambda: self.openwindow(29))
        self.chapter6_test.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter6_test.setObjectName("chapter6_test")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label7 = QtWidgets.QLabel(self.page_7)
        self.label7.setGeometry(QtCore.QRect(180, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.splitter_8 = QtWidgets.QSplitter(self.page_7)
        self.splitter_8.setGeometry(QtCore.QRect(10, 70, 511, 711))
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.chapter7_1 = QtWidgets.QPushButton(self.splitter_8, clicked=lambda: self.openwindow(119))
        self.chapter7_1.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(135, 255, 7);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter7_1.setObjectName("chapter7_1")
        self.chapter7_2 = QtWidgets.QPushButton(self.splitter_8, clicked=lambda: self.openwindow(125))
        self.chapter7_2.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(135, 255, 7);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter7_2.setObjectName("chapter7_2")
        self.chapter7_test = QtWidgets.QPushButton(self.splitter_8, clicked=lambda: self.openwindow(29))
        self.chapter7_test.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter7_test.setObjectName("chapter7_test")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label8 = QtWidgets.QLabel(self.page_8)
        self.label8.setGeometry(QtCore.QRect(180, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label8.setFont(font)
        self.label8.setObjectName("label8")
        self.splitter_14 = QtWidgets.QSplitter(self.page_8)
        self.splitter_14.setGeometry(QtCore.QRect(10, 80, 511, 691))
        self.splitter_14.setOrientation(QtCore.Qt.Vertical)
        self.splitter_14.setObjectName("splitter_14")
        self.chapter8_1 = QtWidgets.QPushButton(self.splitter_14, clicked=lambda: self.openwindow(131))
        self.chapter8_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(135, 255, 7);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter8_1.setObjectName("chapter8_1")
        self.chapter8_2 = QtWidgets.QPushButton(self.splitter_14, clicked=lambda: self.openwindow(135))
        self.chapter8_2.setStyleSheet("QPushButton{\n"
"font: 75 18pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(135, 255, 7);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter8_2.setObjectName("chapter8_2")
        self.chapter8_3 = QtWidgets.QPushButton(self.splitter_14, clicked=lambda: self.openwindow(142))
        self.chapter8_3.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(135, 255, 7);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter8_3.setObjectName("chapter8_3")
        self.chapter8_test = QtWidgets.QPushButton(self.splitter_14, clicked=lambda: self.openwindow(29))
        self.chapter8_test.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter8_test.setObjectName("chapter8_test")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label9 = QtWidgets.QLabel(self.page_9)
        self.label9.setGeometry(QtCore.QRect(180, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.splitter_15 = QtWidgets.QSplitter(self.page_9)
        self.splitter_15.setGeometry(QtCore.QRect(10, 58, 511, 721))
        self.splitter_15.setOrientation(QtCore.Qt.Vertical)
        self.splitter_15.setObjectName("splitter_15")
        self.chapter9_1 = QtWidgets.QPushButton(self.splitter_15, clicked=lambda: self.openwindow(155))
        self.chapter9_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(6, 6, 6);\n"
"    background-color: rgb(0, 255, 191);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter9_1.setObjectName("chapter9_1")
        self.chapter9_2 = QtWidgets.QPushButton(self.splitter_15, clicked=lambda: self.openwindow(159))
        self.chapter9_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(6, 6, 6);\n"
"    background-color: rgb(0, 255, 191);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter9_2.setObjectName("chapter9_2")
        self.chapter9_3 = QtWidgets.QPushButton(self.splitter_15, clicked=lambda: self.openwindow(167))
        self.chapter9_3.setStyleSheet("QPushButton{\n"
"font: 75 15pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(6, 6, 6);\n"
"    background-color: rgb(0, 255, 191);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter9_3.setObjectName("chapter9_3")
        self.chapter9_test = QtWidgets.QPushButton(self.splitter_15, clicked=lambda: self.openwindow(29))
        self.chapter9_test.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter9_test.setObjectName("chapter9_test")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label9_12 = QtWidgets.QLabel(self.page_10)
        self.label9_12.setGeometry(QtCore.QRect(170, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label9_12.setFont(font)
        self.label9_12.setObjectName("label9_12")
        self.splitter_16 = QtWidgets.QSplitter(self.page_10)
        self.splitter_16.setGeometry(QtCore.QRect(10, 70, 511, 711))
        self.splitter_16.setOrientation(QtCore.Qt.Vertical)
        self.splitter_16.setObjectName("splitter_16")
        self.chapter10_1 = QtWidgets.QPushButton(self.splitter_16, clicked=lambda: self.openwindow(172))
        self.chapter10_1.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(6, 6, 6);\n"
"    background-color: rgb(0, 255, 191);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter10_1.setObjectName("chapter10_1")
        self.chapter10_2 = QtWidgets.QPushButton(self.splitter_16, clicked=lambda: self.openwindow(180))
        self.chapter10_2.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(6, 6, 6);\n"
"    background-color: rgb(0, 255, 191);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter10_2.setObjectName("chapter10_2")
        self.chapter10_test = QtWidgets.QPushButton(self.splitter_16, clicked=lambda: self.openwindow(29))
        self.chapter10_test.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter10_test.setObjectName("chapter10_test")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label9_13 = QtWidgets.QLabel(self.page_11)
        self.label9_13.setGeometry(QtCore.QRect(170, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label9_13.setFont(font)
        self.label9_13.setObjectName("label9_13")
        self.splitter_27 = QtWidgets.QSplitter(self.page_11)
        self.splitter_27.setGeometry(QtCore.QRect(10, 100, 511, 681))
        self.splitter_27.setOrientation(QtCore.Qt.Vertical)
        self.splitter_27.setObjectName("splitter_27")
        self.chapter11_1 = QtWidgets.QPushButton(self.splitter_27, clicked=lambda: self.openwindow(195))
        self.chapter11_1.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(8, 201, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter11_1.setObjectName("chapter11_1")
        self.chapter11_2 = QtWidgets.QPushButton(self.splitter_27, clicked=lambda: self.openwindow(200))
        self.chapter11_2.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(8, 201, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter11_2.setObjectName("chapter11_2")
        self.chapter11_3 = QtWidgets.QPushButton(self.splitter_27, clicked=lambda: self.openwindow(205))
        self.chapter11_3.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(8, 201, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter11_3.setObjectName("chapter11_3")
        self.chapter11_test = QtWidgets.QPushButton(self.splitter_27, clicked=lambda: self.openwindow(29))
        self.chapter11_test.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter11_test.setObjectName("chapter11_test")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.label9_14 = QtWidgets.QLabel(self.page_12)
        self.label9_14.setGeometry(QtCore.QRect(170, 30, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label9_14.setFont(font)
        self.label9_14.setObjectName("label9_14")
        self.splitter_28 = QtWidgets.QSplitter(self.page_12)
        self.splitter_28.setGeometry(QtCore.QRect(10, 100, 511, 691))
        self.splitter_28.setOrientation(QtCore.Qt.Vertical)
        self.splitter_28.setObjectName("splitter_28")
        self.chapter12_1 = QtWidgets.QPushButton(self.splitter_28, clicked=lambda: self.openwindow(211))
        self.chapter12_1.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(8, 201, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter12_1.setObjectName("chapter12_1")
        self.chapter12_2 = QtWidgets.QPushButton(self.splitter_28, clicked=lambda: self.openwindow(219))
        self.chapter12_2.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(8, 201, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter12_2.setObjectName("chapter12_2")
        self.chapter12_test = QtWidgets.QPushButton(self.splitter_28, clicked=lambda: self.openwindow(29))
        self.chapter12_test.setStyleSheet("QPushButton{\n"
"font: 75 25pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter12_test.setObjectName("chapter12_test")
        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.label9_15 = QtWidgets.QLabel(self.page_13)
        self.label9_15.setGeometry(QtCore.QRect(180, 30, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label9_15.setFont(font)
        self.label9_15.setObjectName("label9_15")
        self.splitter_29 = QtWidgets.QSplitter(self.page_13)
        self.splitter_29.setGeometry(QtCore.QRect(8, 80, 511, 701))
        self.splitter_29.setOrientation(QtCore.Qt.Vertical)
        self.splitter_29.setObjectName("splitter_29")
        self.chapter13_1 = QtWidgets.QPushButton(self.splitter_29, clicked=lambda: self.openwindow(236))
        self.chapter13_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(217, 0, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter13_1.setObjectName("chapter13_1")
        self.chapter13_2 = QtWidgets.QPushButton(self.splitter_29, clicked=lambda: self.openwindow(243))
        self.chapter13_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(217, 0, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter13_2.setObjectName("chapter13_2")
        self.chapter13_3 = QtWidgets.QPushButton(self.splitter_29, clicked=lambda: self.openwindow(250))
        self.chapter13_3.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(217, 0, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter13_3.setObjectName("chapter13_3")
        self.chapter13_test = QtWidgets.QPushButton(self.splitter_29, clicked=lambda: self.openwindow(29))
        self.chapter13_test.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter13_test.setObjectName("chapter13_test")
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.label9_16 = QtWidgets.QLabel(self.page_14)
        self.label9_16.setGeometry(QtCore.QRect(180, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label9_16.setFont(font)
        self.label9_16.setObjectName("label9_16")
        self.splitter_30 = QtWidgets.QSplitter(self.page_14)
        self.splitter_30.setGeometry(QtCore.QRect(5, 78, 521, 711))
        self.splitter_30.setOrientation(QtCore.Qt.Vertical)
        self.splitter_30.setObjectName("splitter_30")
        self.chapter14_1 = QtWidgets.QPushButton(self.splitter_30, clicked=lambda: self.openwindow(257))
        self.chapter14_1.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(217, 0, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter14_1.setObjectName("chapter14_1")
        self.chapter14_2 = QtWidgets.QPushButton(self.splitter_30, clicked=lambda: self.openwindow(262))
        self.chapter14_2.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(217, 0, 255);\n"
"\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter14_2.setObjectName("chapter14_2")
        self.chapter14_test = QtWidgets.QPushButton(self.splitter_30, clicked=lambda: self.openwindow(29))
        self.chapter14_test.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(61, 217, 245), stop:1 rgb(240, 53, 218));\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}")
        self.chapter14_test.setObjectName("chapter14_test")
        self.stackedWidget.addWidget(self.page_14)
        NewWindow1.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewWindow1)
        self.stackedWidget.setCurrentIndex(13)
        QtCore.QMetaObject.connectSlotsByName(NewWindow1)

    def retranslateUi(self, NewWindow1):
        _translate = QtCore.QCoreApplication.translate
        NewWindow1.setWindowTitle(_translate("NewWindow1", "MainWindow"))
        self.label_2.setText(_translate("NewWindow1", "CHAPTER 1"))
        self.chapter1_1.setText(_translate("NewWindow1", "키워드 (Keyword)"))
        self.chapter1_2.setText(_translate("NewWindow1", "식별자 (Identifier)"))
        self.chapter1_3.setText(_translate("NewWindow1", "들여쓰기 (Indentation)"))
        self.chapter1_4.setText(_translate("NewWindow1", "주석 (Comment)"))
        self.chapter1_test.setText(_translate("NewWindow1", "TEST"))
        self.label2.setText(_translate("NewWindow1", "CHAPTER 2"))
        self.chapter2_1.setText(_translate("NewWindow1", "변수 선언과 할당"))
        self.chapter2_2.setText(_translate("NewWindow1", "변수 이름 정하기"))
        self.chapter2_test.setText(_translate("NewWindow1", "TEST"))
        self.label3.setText(_translate("NewWindow1", "CHAPTER 3"))
        self.chapter3_1.setText(_translate("NewWindow1", "연산자 "))
        self.chapter3_test.setText(_translate("NewWindow1", "TEST"))
        self.label4.setText(_translate("NewWindow1", "CHAPTER 4"))
        self.chapter4_1.setText(_translate("NewWindow1", "리스트 기초"))
        self.chapter4_2.setText(_translate("NewWindow1", "리스트 정렬"))
        self.chapter4_3.setText(_translate("NewWindow1", "리스트 슬라이싱"))
        self.chapter4_4.setText(_translate("NewWindow1", "리스트 컴프리헨션"))
        self.chapter4_5.setText(_translate("NewWindow1", "리스트 메서드"))
        self.chapter4_test.setText(_translate("NewWindow1", "TEST"))
        self.label5.setText(_translate("NewWindow1", "CHAPTER 5"))
        self.chapter5_1.setText(_translate("NewWindow1", "튜플 "))
        self.chapter5_test.setText(_translate("NewWindow1", "TEST"))
        self.label6.setText(_translate("NewWindow1", "CHAPTER 6"))
        self.chapter6_1.setText(_translate("NewWindow1", "문자열"))
        self.chapter6_2.setText(_translate("NewWindow1", "문자열 메서드"))
        self.chapter6_3.setText(_translate("NewWindow1", "문자열 메서드 2"))
        self.chapter6_test.setText(_translate("NewWindow1", "TEST"))
        self.label7.setText(_translate("NewWindow1", "CHAPTER 7"))
        self.chapter7_1.setText(_translate("NewWindow1", "집합 "))
        self.chapter7_2.setText(_translate("NewWindow1", "집합 값 삭제하기"))
        self.chapter7_test.setText(_translate("NewWindow1", "TEST"))
        self.label8.setText(_translate("NewWindow1", "CHAPTER 8"))
        self.chapter8_1.setText(_translate("NewWindow1", "딕셔너리"))
        self.chapter8_2.setText(_translate("NewWindow1", "딕셔너리 아이템 추가 및 삭제하기"))
        self.chapter8_3.setText(_translate("NewWindow1", "딕셔너리 루프와 메서드"))
        self.chapter8_test.setText(_translate("NewWindow1", "TEST"))
        self.label9.setText(_translate("NewWindow1", "CHAPTER 9"))
        self.chapter9_1.setText(_translate("NewWindow1", "if 문"))
        self.chapter9_2.setText(_translate("NewWindow1", "for 문/while문"))
        self.chapter9_3.setText(_translate("NewWindow1", "break 문 / continue 문/pass 문"))
        self.chapter9_test.setText(_translate("NewWindow1", "TEST"))
        self.label9_12.setText(_translate("NewWindow1", "CHAPTER 10"))
        self.chapter10_1.setText(_translate("NewWindow1", "함수 / 매개변수"))
        self.chapter10_2.setText(_translate("NewWindow1", "키워드인자"))
        self.chapter10_test.setText(_translate("NewWindow1", "TEST"))
        self.label9_13.setText(_translate("NewWindow1", "CHAPTER 11"))
        self.chapter11_1.setText(_translate("NewWindow1", "클래스 기초"))
        self.chapter11_2.setText(_translate("NewWindow1", "클래스 속성 다루기"))
        self.chapter11_3.setText(_translate("NewWindow1", "클래스 상속"))
        self.chapter11_test.setText(_translate("NewWindow1", "TEST"))
        self.label9_14.setText(_translate("NewWindow1", "CHAPTER 12"))
        self.chapter12_1.setText(_translate("NewWindow1", "파이썬 내장함수 1"))
        self.chapter12_2.setText(_translate("NewWindow1", "파이썬 내장함수 2"))
        self.chapter12_test.setText(_translate("NewWindow1", "TEST"))
        self.label9_15.setText(_translate("NewWindow1", "CHAPTER 13"))
        self.chapter13_1.setText(_translate("NewWindow1", "Python 키워드 (Keyword)1"))
        self.chapter13_2.setText(_translate("NewWindow1", "Python 키워드 (Keyword) 2"))
        self.chapter13_3.setText(_translate("NewWindow1", "Python 키워드 (Keyword) 3"))
        self.chapter13_test.setText(_translate("NewWindow1", "TEST"))
        self.label9_16.setText(_translate("NewWindow1", "CHAPTER 14"))
        self.chapter14_1.setText(_translate("NewWindow1", "Python 파일 다루기 "))
        self.chapter14_2.setText(_translate("NewWindow1", "Python 파일 다루기 2"))
        self.chapter14_test.setText(_translate("NewWindow1", "TEST"))
    def run_2py(self):
        subprocess.run(['python', 'quiz.py'])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewWindow1 = QtWidgets.QMainWindow()
    ui = Ui_NewWindow1()
    ui.setupUi(NewWindow1)
    NewWindow1.show()
    sys.exit(app.exec_())
