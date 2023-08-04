
from PyQt5 import QtCore, QtGui, QtWidgets
##
from newwindow import Ui_NewWindow1


class Ui_MainWindow(object):
    ##새창열기함수
    def openwindow(self, index):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewWindow1()
        self.ui.setupUi(self.window)
        self.window.show()
        ## 페이지 번호지정
        self.ui.stackedWidget.setCurrentIndex(index)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("/*= Style for mainwindow START\n"
"  ==================================================== */\n"
"    #MainWindow {\n"
"        background-color: #fff;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for button to change menu style START\n"
"  ==================================================== */\n"
"    #change_btn {\n"
"        padding: 5px;\n"
"        border: none;\n"
"        width: 30px;\n"
"        height: 30px;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for header widget START\n"
"  ==================================================== */\n"
"    #widget {\n"
"        background-color: #f9fafd;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for menu with icon only START\n"
"  ==================================================== */\n"
"      /* style for widget */\n"
"    #icon_only_widget {\n"
"        background-color: #313a46;\n"
"        width:50px;\n"
"    }\n"
"\n"
"    /* style for QPushButton and QLabel */\n"
"    #icon_only_widget QPushButton, QLabel {\n"
"        height:50px;\n"
"        border:none;\n"
"        /* border-bottom: 1px solid #b0b0b0; */\n"
"    }\n"
"\n"
"    #icon_only_widget QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }\n"
"\n"
"    /* style for logo image */\n"
"    #logo_label_1 {\n"
"        padding: 5px\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for menu with icon and text START\n"
"  ==================================================== */\n"
"    /* style for widget */\n"
"    #full_menu_widget {\n"
"        background-color: #313a46;\n"
"    }\n"
"\n"
"    /* style for QPushButton */\n"
"    #full_menu_widget QPushButton {\n"
"        border:none;\n"
"        border-radius: 3px;\n"
"        text-align: left;\n"
"        padding: 8px 0 8px 15px;\n"
"        color: #788596;\n"
"    }\n"
"\n"
"    #full_menu_widget QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }\n"
"\n"
"    #full_menu_widget QPushButton:checked {\n"
"        color: #fff;\n"
"    }\n"
"\n"
"    /* style for logo image */\n"
"    #logo_label_2 {\n"
"        padding: 5px;\n"
"        color: #fff;\n"
"    }\n"
"\n"
"    /* style for APP title */\n"
"    #logo_label_3 {\n"
"        padding-right: 10px;\n"
"        color: #fff;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for search button START\n"
"  ==================================================== */\n"
"    #search_btn {\n"
"        border: none;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for search input START\n"
"  ==================================================== */\n"
"    #search_input {\n"
"        border: none;\n"
"        padding: 5px 10px;\n"
"    }\n"
"\n"
"    #search_input:focus {\n"
"        background-color: #70B9FE;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for user information button START\n"
"  ==================================================== */\n"
"    #user_btn {\n"
"        border: none;\n"
"    }\n"
"/*= END\n"
"  ==================================================== */")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setMaximumSize(QtCore.QSize(50, 50))
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.dashborad_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.dashborad_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/dashboard-5-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dashborad_btn_1.setIcon(icon1)
        self.dashborad_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.dashborad_btn_1.setCheckable(True)
        self.dashborad_btn_1.setAutoExclusive(True)
        self.dashborad_btn_1.setObjectName("dashborad_btn_1")
        self.verticalLayout.addWidget(self.dashborad_btn_1)
        self.orders_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.orders_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/activity-feed-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.orders_btn_1.setIcon(icon2)
        self.orders_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.orders_btn_1.setCheckable(True)
        self.orders_btn_1.setAutoExclusive(True)
        self.orders_btn_1.setObjectName("orders_btn_1")
        self.verticalLayout.addWidget(self.orders_btn_1)
        self.products_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.products_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/product-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/icon/product-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.products_btn_1.setIcon(icon3)
        self.products_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.products_btn_1.setCheckable(True)
        self.products_btn_1.setAutoExclusive(True)
        self.products_btn_1.setObjectName("products_btn_1")
        self.verticalLayout.addWidget(self.products_btn_1)
        self.customers_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.customers_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/group-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/icon/group-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.customers_btn_1.setIcon(icon4)
        self.customers_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.customers_btn_1.setCheckable(True)
        self.customers_btn_1.setAutoExclusive(True)
        self.customers_btn_1.setObjectName("customers_btn_1")
        self.verticalLayout.addWidget(self.customers_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.dashborad_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.dashborad_btn_2.setIcon(icon1)
        self.dashborad_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.dashborad_btn_2.setCheckable(True)
        self.dashborad_btn_2.setAutoExclusive(True)
        self.dashborad_btn_2.setObjectName("dashborad_btn_2")
        self.verticalLayout_2.addWidget(self.dashborad_btn_2)
        self.orders_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.orders_btn_2.setIcon(icon2)
        self.orders_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.orders_btn_2.setCheckable(True)
        self.orders_btn_2.setAutoExclusive(True)
        self.orders_btn_2.setObjectName("orders_btn_2")
        self.verticalLayout_2.addWidget(self.orders_btn_2)
        self.products_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.products_btn_2.setIcon(icon3)
        self.products_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)
        self.products_btn_2.setObjectName("products_btn_2")
        self.verticalLayout_2.addWidget(self.products_btn_2)
        self.customers_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.customers_btn_2.setIcon(icon4)
        self.customers_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)
        self.customers_btn_2.setObjectName("customers_btn_2")
        self.verticalLayout_2.addWidget(self.customers_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QtCore.QSize(14, 14))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/menu-4-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QtCore.QSize(14, 14))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget)
        self.search_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/icon/search-13-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon7)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.user_btn = QtWidgets.QPushButton(self.widget)
        self.user_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icon/icon/user-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon8)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_4.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.chapter3 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(2))
        self.chapter3.setGeometry(QtCore.QRect(350, 20, 161, 131))
        self.chapter3.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter3.setObjectName("chapter3")
        self.chapter4 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(3))
        self.chapter4.setGeometry(QtCore.QRect(520, 20, 161, 131))
        self.chapter4.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter4.setObjectName("chapter4")
        self.chapter2 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(1))
        self.chapter2.setGeometry(QtCore.QRect(180, 20, 161, 131))
        self.chapter2.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter2.setObjectName("chapter2")
        self.chapter8 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(7))
        self.chapter8.setGeometry(QtCore.QRect(520, 160, 161, 131))
        self.chapter8.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter8.setObjectName("chapter8")
        self.chapter1 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(0))
        self.chapter1.setGeometry(QtCore.QRect(10, 20, 161, 131))
        self.chapter1.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter1.setObjectName("chapter1")
        self.chapter9 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(8))
        self.chapter9.setGeometry(QtCore.QRect(10, 300, 161, 131))
        self.chapter9.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter9.setObjectName("chapter9")
        self.chapter5 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(4))
        self.chapter5.setGeometry(QtCore.QRect(10, 160, 161, 131))
        self.chapter5.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter5.setObjectName("chapter5")
        self.chapter6 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(5))
        self.chapter6.setGeometry(QtCore.QRect(180, 160, 161, 131))
        self.chapter6.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter6.setObjectName("chapter6")
        self.chapter7 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(6))
        self.chapter7.setGeometry(QtCore.QRect(350, 160, 161, 131))
        self.chapter7.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter7.setObjectName("chapter7")
        self.chapter13 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(12))
        self.chapter13.setGeometry(QtCore.QRect(10, 440, 161, 131))
        self.chapter13.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter13.setObjectName("chapter13")
        self.chapter10 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(9))
        self.chapter10.setGeometry(QtCore.QRect(180, 300, 161, 131))
        self.chapter10.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter10.setObjectName("chapter10")
        self.chapter14 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(13))
        self.chapter14.setGeometry(QtCore.QRect(180, 440, 161, 131))
        self.chapter14.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter14.setObjectName("chapter14")
        self.chapter11 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(10))
        self.chapter11.setGeometry(QtCore.QRect(350, 300, 161, 131))
        self.chapter11.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter11.setObjectName("chapter11")
        self.chapter12 = QtWidgets.QPushButton(self.page,clicked=lambda: self.openwindow(11))
        self.chapter12.setGeometry(QtCore.QRect(520, 300, 161, 131))
        self.chapter12.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter12.setObjectName("chapter12")
        self.chapter15 = QtWidgets.QPushButton(self.page)
        self.chapter15.setGeometry(QtCore.QRect(350, 440, 161, 131))
        self.chapter15.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter15.setObjectName("chapter15")
        self.chapter16 = QtWidgets.QPushButton(self.page)
        self.chapter16.setGeometry(QtCore.QRect(520, 440, 161, 131))
        self.chapter16.setStyleSheet("QPushButton{\n"
"    font: 15pt \"Microsoft YaHei UI\";\n"
"    color: white;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
"    border-radius: 20px;\n"
"}")
        self.chapter16.setObjectName("chapter16")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_8 = QtWidgets.QLabel(self.page_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_9 = QtWidgets.QLabel(self.page_6)
        self.label_9.setGeometry(QtCore.QRect(10, 0, 689, 516))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(self.page_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.dashborad_btn_1.toggled['bool'].connect(self.dashborad_btn_2.setChecked) # type: ignore
        self.orders_btn_1.toggled['bool'].connect(self.orders_btn_2.setChecked) # type: ignore
        self.products_btn_1.toggled['bool'].connect(self.products_btn_2.setChecked) # type: ignore
        self.customers_btn_1.toggled['bool'].connect(self.customers_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.dashborad_btn_2.toggled['bool'].connect(self.dashborad_btn_1.setChecked) # type: ignore
        self.orders_btn_2.toggled['bool'].connect(self.orders_btn_1.setChecked) # type: ignore
        self.products_btn_2.toggled['bool'].connect(self.products_btn_1.setChecked) # type: ignore
        self.customers_btn_2.toggled['bool'].connect(self.customers_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logo_label_3.setText(_translate("MainWindow", "Sidebar"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.dashborad_btn_2.setText(_translate("MainWindow", "Dashboard"))
        self.orders_btn_2.setText(_translate("MainWindow", "Orders"))
        self.products_btn_2.setText(_translate("MainWindow", "Products"))
        self.customers_btn_2.setText(_translate("MainWindow", "Customers"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.chapter3.setText(_translate("MainWindow", "CHAPTER 3"))
        self.chapter4.setText(_translate("MainWindow", "CHAPTER 4"))
        self.chapter2.setText(_translate("MainWindow", "CHAPTER 2"))
        self.chapter8.setText(_translate("MainWindow", "CHAPTER 8"))
        self.chapter1.setText(_translate("MainWindow", "CHAPTER 1"))
        self.chapter9.setText(_translate("MainWindow", "CHAPTER 9"))
        self.chapter5.setText(_translate("MainWindow", "CHAPTER 5"))
        self.chapter6.setText(_translate("MainWindow", "CHAPTER 6"))
        self.chapter7.setText(_translate("MainWindow", "CHAPTER 7"))
        self.chapter13.setText(_translate("MainWindow", "CHAPTER 13"))
        self.chapter10.setText(_translate("MainWindow", "CHAPTER 10"))
        self.chapter14.setText(_translate("MainWindow", "CHAPTER 14"))
        self.chapter11.setText(_translate("MainWindow", "CHAPTER 11"))
        self.chapter12.setText(_translate("MainWindow", "CHAPTER 12"))
        self.chapter15.setText(_translate("MainWindow", "FINAL TEST1"))
        self.chapter16.setText(_translate("MainWindow", "FINAL TEST2"))
        self.label_5.setText(_translate("MainWindow", "Dashboard Page"))
        self.label_6.setText(_translate("MainWindow", "Orders Page"))
        self.label_7.setText(_translate("MainWindow", "Product Page"))
        self.label_8.setText(_translate("MainWindow", "Customers Page"))
        self.label_9.setText(_translate("MainWindow", "검색결과가 존재하지 않습니다"))
        self.label_10.setText(_translate("MainWindow", "User Page"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
