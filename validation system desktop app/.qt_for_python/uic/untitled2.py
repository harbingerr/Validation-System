# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled2.ui'
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
        MainWindow.resize(771, 523)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 747, 448))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.card = QFrame(self.scrollAreaWidgetContents)
        self.card.setObjectName(u"card")
        self.card.setMinimumSize(QSize(200, 300))
        self.card.setMaximumSize(QSize(300, 400))
        self.card.setStyleSheet(u"border-radius: 25% 10%;\n"
"background-color: rgb(158, 158, 158);\n"
"border-style: solid;")
        self.card.setFrameShape(QFrame.StyledPanel)
        self.card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.card)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.card)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(112, 112, 112);\n"
"border-bottom-left-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom: 6px groove;\n"
"border-bottom-color: rgb(58, 58, 58);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.header_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_scenario_name = QLabel(self.header_frame)
        self.lb_scenario_name.setObjectName(u"lb_scenario_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_scenario_name.setFont(font)
        self.lb_scenario_name.setStyleSheet(u"border-bottom: hidden;\n"
"color: rgb(235, 235, 235);\n"
"")

        self.gridLayout_2.addWidget(self.lb_scenario_name, 0, 0, 2, 1)


        self.verticalLayout_2.addWidget(self.header_frame)

        self.progress_frame = QFrame(self.card)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.progress_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_complete = QLabel(self.progress_frame)
        self.lb_complete.setObjectName(u"lb_complete")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.lb_complete.setFont(font1)

        self.verticalLayout_3.addWidget(self.lb_complete, 0, Qt.AlignHCenter)

        self.progressBar = QProgressBar(self.progress_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.progress_frame, 0, Qt.AlignTop)

        self.footer_frame = QFrame(self.card)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.footer_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_start = QPushButton(self.footer_frame)
        self.bt_start.setObjectName(u"bt_start")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.bt_start.sizePolicy().hasHeightForWidth())
        self.bt_start.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        self.bt_start.setFont(font2)
        self.bt_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_start.setStyleSheet(u"background-color: rgb(7, 226, 87);")

        self.horizontalLayout.addWidget(self.bt_start)


        self.verticalLayout_2.addWidget(self.footer_frame)


        self.gridLayout.addWidget(self.card, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 200))
        self.frame_2.setMaximumSize(QSize(300, 300))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 771, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_scenario_name.setText(QCoreApplication.translate("MainWindow", u"Scenario 1 Name", None))
        self.lb_complete.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
        self.bt_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

