# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledpMueHb.ui'
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

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 20, -1, -1)
        self.lb_scenario_name_in_task_header = QLabel(self.tasks_header)
        self.lb_scenario_name_in_task_header.setObjectName(u"lb_scenario_name_in_task_header")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.lb_scenario_name_in_task_header.setFont(font2)
        self.lb_scenario_name_in_task_header.setMargin(9)

        self.verticalLayout_8.addWidget(self.lb_scenario_name_in_task_header)

        self.lb_validation_spet_in_task_header = QLabel(self.tasks_header)
        self.lb_validation_spet_in_task_header.setObjectName(u"lb_validation_spet_in_task_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_validation_spet_in_task_header.sizePolicy().hasHeightForWidth())
        self.lb_validation_spet_in_task_header.setSizePolicy(sizePolicy2)
        self.lb_validation_spet_in_task_header.setMargin(10)

        self.verticalLayout_8.addWidget(self.lb_validation_spet_in_task_header)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)

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
        self.bt_show_desc = QPushButton(self.task)
        self.bt_show_desc.setObjectName(u"bt_show_desc")
        sizePolicy2.setHeightForWidth(self.bt_show_desc.sizePolicy().hasHeightForWidth())
        self.bt_show_desc.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.bt_show_desc.setFont(font3)
        self.bt_show_desc.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_show_desc.setStyleSheet(u"background-color: rgb(149, 149, 149);\n"
"text-align: left;\n"
"padding: 15px 10px;")
        icon3 = QIcon()
        icon3.addFile(u"icons/icons8-menu-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_show_desc.setIcon(icon3)

        self.verticalLayout_7.addWidget(self.bt_show_desc)

        self.scrollArea_3 = QScrollArea(self.task)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setEnabled(True)
        self.scrollArea_3.setMaximumSize(QSize(16777215, 200))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 756, 200))
        self.scrollAreaWidgetContents_3.setMinimumSize(QSize(0, 200))
        self.scrollAreaWidgetContents_3.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb_task_description = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_task_description.setObjectName(u"lb_task_description")
        sizePolicy2.setHeightForWidth(self.lb_task_description.sizePolicy().hasHeightForWidth())
        self.lb_task_description.setSizePolicy(sizePolicy2)
        self.lb_task_description.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.lb_task_description)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit.setStyleSheet(u"background-color: rgb(223, 223, 223);\n"
"padding: 0px 10px;")

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.bt_submit = QPushButton(self.frame_7)
        self.bt_submit.setObjectName(u"bt_submit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bt_submit.sizePolicy().hasHeightForWidth())
        self.bt_submit.setSizePolicy(sizePolicy4)
        self.bt_submit.setMinimumSize(QSize(0, 40))
        self.bt_submit.setFont(font3)
        self.bt_submit.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_submit.setStyleSheet(u"background-color: rgb(22, 30, 45);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        icon4 = QIcon()
        icon4.addFile(u"icons/white/icons8-play-button-circled-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_submit.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.bt_submit)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.lb_success_message = QLabel(self.scrollAreaWidgetContents_3)
        self.lb_success_message.setObjectName(u"lb_success_message")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lb_success_message.sizePolicy().hasHeightForWidth())
        self.lb_success_message.setSizePolicy(sizePolicy5)
        self.lb_success_message.setStyleSheet(u"color: rgb(49, 255, 3);")

        self.verticalLayout_9.addWidget(self.lb_success_message)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_7.addWidget(self.scrollArea_3)


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
        font4 = QFont()
        font4.setPointSize(8)
        self.lb_cp.setFont(font4)

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
        self.lb_desc.setText(QCoreApplication.translate("MainWindow", u"This learning path covers the core technical skills that will allow you to succeed as a junior penetration tester. Upon completing this path, you will have the practical skills necessary to perform security assessments against virtual network.", None))
        self.bt_back.setText("")
        self.lb_scenario_name_in_task_header.setText(QCoreApplication.translate("MainWindow", u"Scenario XY", None))
        self.lb_validation_spet_in_task_header.setText(QCoreApplication.translate("MainWindow", u"Task XY", None))
        self.bt_show_desc.setText(QCoreApplication.translate("MainWindow", u"Task 1", None))
        self.lb_task_description.setText(QCoreApplication.translate("MainWindow", u"Description text", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Answer the question", None))
        self.bt_submit.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.lb_success_message.setText(QCoreApplication.translate("MainWindow", u"Success", None))
        self.lb_cp.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2022", None))
    # retranslateUi

