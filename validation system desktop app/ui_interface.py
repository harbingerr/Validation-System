# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledosVfnz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"background-color: rgb(22, 30, 45);")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_left)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, -1, 50, 11)
        self.lb_icon = QLabel(self.header_left)
        self.lb_icon.setObjectName(u"lb_icon")
        self.lb_icon.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lb_icon.setPixmap(QPixmap(u"icons/white/icons8-system-information-50.png"))

        self.horizontalLayout_3.addWidget(self.lb_icon, 0, Qt.AlignLeft)

        self.lb_validation_system = QLabel(self.header_left)
        self.lb_validation_system.setObjectName(u"lb_validation_system")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lb_validation_system.setFont(font)
        self.lb_validation_system.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.lb_validation_system, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.header_left)

        self.header_right = QFrame(self.header)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.bt_minimize_window = QPushButton(self.header_right)
        self.bt_minimize_window.setObjectName(u"bt_minimize_window")
        self.bt_minimize_window.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"icons/white/icons8-minus-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimize_window.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.bt_minimize_window)

        self.bt_close_window = QPushButton(self.header_right)
        self.bt_close_window.setObjectName(u"bt_close_window")
        self.bt_close_window.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"icons/white/icons8-close-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close_window.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.bt_close_window)


        self.horizontalLayout.addWidget(self.header_right, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sw_header = QStackedWidget(self.main)
        self.sw_header.setObjectName(u"sw_header")
        self.sw_header.setStyleSheet(u"background-color: rgb(208, 208, 208);")
        self.scenarios_header = QWidget()
        self.scenarios_header.setObjectName(u"scenarios_header")
        self.verticalLayout_3 = QVBoxLayout(self.scenarios_header)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_header = QFrame(self.scenarios_header)
        self.main_header.setObjectName(u"main_header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_header.sizePolicy().hasHeightForWidth())
        self.main_header.setSizePolicy(sizePolicy1)
        self.main_header.setMinimumSize(QSize(756, 0))
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_header)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_redhead_icon = QLabel(self.main_header)
        self.lb_redhead_icon.setObjectName(u"lb_redhead_icon")
        self.lb_redhead_icon.setMaximumSize(QSize(378, 16777215))
        self.lb_redhead_icon.setPixmap(QPixmap(u"icons/icons8-red-hat-50.png"))

        self.horizontalLayout_5.addWidget(self.lb_redhead_icon, 0, Qt.AlignHCenter)

        self.lb_title = QLabel(self.main_header)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setFont(font)

        self.horizontalLayout_5.addWidget(self.lb_title)

        self.frame_5 = QFrame(self.main_header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.main_header)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.main_header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.main_header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame = QFrame(self.main_header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.main_header)

        self.lb_desc = QLabel(self.scenarios_header)
        self.lb_desc.setObjectName(u"lb_desc")
        font1 = QFont()
        font1.setPointSize(9)
        self.lb_desc.setFont(font1)
        self.lb_desc.setStyleSheet(u"color: rgb(61, 61, 61);")
        self.lb_desc.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.lb_desc)

        self.sw_header.addWidget(self.scenarios_header)
        self.tasks_header = QWidget()
        self.tasks_header.setObjectName(u"tasks_header")
        self.horizontalLayout_6 = QHBoxLayout(self.tasks_header)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_back = QPushButton(self.tasks_header)
        self.bt_back.setObjectName(u"bt_back")
        self.bt_back.setMinimumSize(QSize(50, 0))
        self.bt_back.setMaximumSize(QSize(50, 16777215))
        self.bt_back.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"icons/icons8-back-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_back.setIcon(icon2)
        self.bt_back.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.bt_back)

        self.lb_scenario_name_in_task_header = QLabel(self.tasks_header)
        self.lb_scenario_name_in_task_header.setObjectName(u"lb_scenario_name_in_task_header")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.lb_scenario_name_in_task_header.setFont(font2)

        self.horizontalLayout_6.addWidget(self.lb_scenario_name_in_task_header)

        self.sw_header.addWidget(self.tasks_header)

        self.verticalLayout_2.addWidget(self.sw_header, 0, Qt.AlignTop)

        self.sw_lists = QStackedWidget(self.main)
        self.sw_lists.setObjectName(u"sw_lists")
        self.scenarios = QWidget()
        self.scenarios.setObjectName(u"scenarios")
        self.verticalLayout_4 = QVBoxLayout(self.scenarios)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.scenarios)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 778, 335))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.card = QFrame(self.scrollAreaWidgetContents)
        self.card.setObjectName(u"card")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.card.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.card, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.sw_lists.addWidget(self.scenarios)
        self.tasks = QWidget()
        self.tasks.setObjectName(u"tasks")
        self.verticalLayout_5 = QVBoxLayout(self.tasks)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea_2 = QScrollArea(self.tasks)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 778, 335))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.task = QFrame(self.scrollAreaWidgetContents_2)
        self.task.setObjectName(u"task")
        self.task.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.task.setFrameShape(QFrame.StyledPanel)
        self.task.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.task)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_6.addWidget(self.task)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_2)

        self.sw_lists.addWidget(self.tasks)

        self.verticalLayout_2.addWidget(self.sw_lists)


        self.verticalLayout.addWidget(self.main)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_cp = QLabel(self.footer)
        self.lb_cp.setObjectName(u"lb_cp")
        font3 = QFont()
        font3.setPointSize(8)
        self.lb_cp.setFont(font3)

        self.horizontalLayout_4.addWidget(self.lb_cp, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_icon.setText("")
        self.lb_validation_system.setText(QCoreApplication.translate("MainWindow", u"Validation System", None))
        self.bt_minimize_window.setText("")
        self.bt_close_window.setText("")
        self.lb_redhead_icon.setText("")
        self.lb_title.setText(QCoreApplication.translate("MainWindow", u"Choose your path", None))
        self.lb_desc.setText(QCoreApplication.translate("MainWindow", u"Choose your learning path which covers the core technical skills that will allow you to succeed as a junior penetration tester. Upon completing this path, you will have various practical skills necessary to perform security assessments against the enterprise infrastructure.", None))
        self.bt_back.setText("")
        self.lb_scenario_name_in_task_header.setText(QCoreApplication.translate("MainWindow", u"Scenario XY", None))
        self.lb_cp.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2022", None))
    # retranslateUi

