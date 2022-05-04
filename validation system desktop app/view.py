from turtle import width
from PySide2 import *
import json
import sys
import os

from ui_untitled_demo import *
from main import *
from constants import *

#########################################
#########################################
## VIEW
#########################################
#########################################

#########################################
## Method to generate one scenario card widget
#########################################
def generateCards2(self, scenario):
    ## Calculating the position based on the id
    positionX = 0 if scenario.id < 4 else 1 
    positionY = (scenario.id - 1) % 3 
    
    self.card = QFrame(self.ui.scrollAreaWidgetContents)
    self.card.setObjectName(u"scenario_" + str(scenario.id))
    self.card.setMinimumSize(QSize(200, 200))
    self.card.setMaximumSize(QSize(300, 300))
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
    self.header_frame.setObjectName(u"header_frame_" + str(scenario.id))
    self.header_frame.setStyleSheet(u"background-color: rgb(112, 112, 112);\n"
    "border-bottom-left-radius: 0px;\n"
    "border-bottom-right-radius: 0px;\n"
    "border-bottom: 6px groove;\n"
    "border-bottom-color: rgb(58, 58, 58);")
    self.header_frame.setFrameShape(QFrame.StyledPanel)
    self.header_frame.setFrameShadow(QFrame.Raised)
    self.gridLayout_2 = QGridLayout(self.header_frame)
    self.gridLayout_2.setObjectName(u"gridLayout_2_" + str(scenario.id))
    self.lb_scenario_name = QLabel(self.header_frame)
    self.lb_scenario_name.setObjectName(u"lb_scenario_name_" + str(scenario.id))
    font = QFont()
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(75)
    self.lb_scenario_name.setFont(font)
    self.lb_scenario_name.setStyleSheet(u"border-bottom: hidden;\n"
    "color: rgb(235, 235, 235);\n"
    "")

    self.gridLayout_2.addWidget(self.lb_scenario_name, 0, 1, 2, 1)


    self.verticalLayout_2.addWidget(self.header_frame)

    self.progress_frame = QFrame(self.card)
    self.progress_frame.setObjectName(u"progress_frame_" + str(scenario.id))
    self.progress_frame.setFrameShape(QFrame.StyledPanel)
    self.progress_frame.setFrameShadow(QFrame.Raised)
    self.verticalLayout_3 = QVBoxLayout(self.progress_frame)
    self.verticalLayout_3.setObjectName(u"verticalLayout_3_" + str(scenario.id))
    self.lb_complete = QLabel(self.progress_frame)
    self.lb_complete.setObjectName("lb_complete_" + str(scenario.id))
    font1 = QFont()
    font1.setPointSize(10)
    font1.setBold(True)
    font1.setWeight(75)
    self.lb_complete.setFont(font1)

    self.verticalLayout_3.addWidget(self.lb_complete, 0, Qt.AlignHCenter)

    self.progressBar = QProgressBar(self.progress_frame)
    self.progressBar.setObjectName(u"progressBar_" + str(scenario.id))
    self.progressBar.setStyleSheet(u"background-color: rgb(232, 232, 232);")
    setattr(self.ui,"progressBar_" + str(scenario.id),self.progressBar)
    ##setting value based on the current progress
    updateProgressBar(self,scenario)

    self.verticalLayout_3.addWidget(self.progressBar)


    self.verticalLayout_2.addWidget(self.progress_frame, 0, Qt.AlignTop)

    self.footer_frame = QFrame(self.card)
    self.footer_frame.setObjectName(u"footer_frame_" + str(scenario.id))
    self.footer_frame.setFrameShape(QFrame.StyledPanel)
    self.footer_frame.setFrameShadow(QFrame.Raised)
    self.horizontalLayout = QHBoxLayout(self.footer_frame)
    self.horizontalLayout.setObjectName(u"horizontalLayout_" + str(scenario.id))
    self.bt_start = QPushButton(self.footer_frame)
    self.bt_start.setObjectName(u"bt_start" + str(scenario.id))
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

    self.lb_scenario_name.setText(QCoreApplication.translate("MainWindow", u""+scenario.title, None))
    self.lb_scenario_name.setWordWrap(True)
    self.lb_complete.setText(QCoreApplication.translate("MainWindow", u"Complete", None))
    self.bt_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))

    ## Activate Start Button
    self.bt_start.clicked.connect(lambda: self.ui.sw_header.setCurrentWidget(self.ui.tasks_header))
    self.bt_start.clicked.connect(lambda: self.ui.sw_lists.setCurrentWidget(self.ui.tasks))
    self.bt_start.clicked.connect(lambda: generateTasks(self, scenario))

    self.ui.gridLayout.addWidget(self.card, positionX, positionY, 1, 1, Qt.AlignHCenter | Qt.AlignVCenter)

#########################################
## Method to generate task widget
#########################################
def generateTasks(self,scenario):
  ##HEADER
  ## Init Button and set Titles
  ## Activate Back Button
  self.ui.bt_back.clicked.connect(lambda: self.ui.sw_header.setCurrentWidget(self.ui.scenarios_header))
  self.ui.bt_back.clicked.connect(lambda: self.ui.sw_lists.setCurrentWidget(self.ui.scenarios))
  self.ui.bt_back.clicked.connect(lambda: calculateCurrent(self, scenario))
  ## Set title
  self.ui.lb_scenario_name_in_task_header.setText(QCoreApplication.translate("MainWindow", scenario.title, None))
  
  ##BODY
  ## Init Previous/Next step buttons and set labels (hide sucess label + update description)
  # Disable previous button on first step and next button on last step
  # Disable next button if the current one is unfinished
  disalbeButtons(self,scenario)
  
  # last argument is representing the flag to distinguish which button was pressed
  self.ui.bt_previous.clicked.connect(lambda: generateTask(self, scenario, -1))
  self.ui.bt_next.clicked.connect(lambda: generateTask(self, scenario, 1))
  generateTask(self, scenario, 0)

#########################################
## Method to disable next/previous button
#########################################
def disalbeButtons(self, scenario):
    # Disable previous button on first step and next button on last step
    # Disable next button if the current one is unfinished
    if(scenario.current == 1):
        self.ui.bt_previous.setEnabled(False)
    else:
        self.ui.bt_previous.setEnabled(True)
    
    validationID = scenario.current - 1
    if(scenario.steps < scenario.current + 1):
        self.ui.bt_next.setEnabled(False)
    elif scenario.validations[validationID + 1].completed == "false":
        self.ui.bt_next.setEnabled(False)
    else:
        self.ui.bt_next.setEnabled(True)

#########################################
## Method to generate one task widget
#########################################
def generateTask(self, scenario, bt_clicked):
    task_to_generate = scenario.validations[0]

    if bt_clicked == 0:
        task_to_generate = scenario.validations[scenario.current - 1]
    elif bt_clicked == 1:
        task_to_generate = scenario.validations[scenario.current]
        scenario.current = task_to_generate.id
        disalbeButtons(self, scenario)
    elif bt_clicked == -1:
        print("We here")
        task_to_generate = scenario.validations[scenario.current - 2]
        scenario.current = task_to_generate.id
        disalbeButtons(self, scenario)

    #Change header 
    self.ui.lb_validation_step_in_task_header.setText(QCoreApplication.translate("MainWindow", u"Task " + str(scenario.current) + " / " + str(scenario.steps), None))
    
    if(task_to_generate.completed == "true"):
        disableUI(self)
    else:
        enableUI(self)    

    ######################################################################
    ## SETTING TEXT AND METHODS 
    ######################################################################
    
    self.ui.lb_description.setText(QCoreApplication.translate("MainWindow", task_to_generate.task, None))
    self.ui.lb_msg_success.setText(QCoreApplication.translate("MainWindow", "", None))
    self.ui.lineEdit.setText(QCoreApplication.translate("MainWindow", "", None))
    
    if(task_to_generate.type == 'flag'):
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert flag", None))
    elif(task_to_generate.type == 'internal command' or 'external command'):
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Submit to start automated test", None))
        self.ui.lineEdit.setReadOnly(True)
    elif(task_to_generate.type == 'none'):
        self.ui.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Submit to continue", None))
        self.ui.lineEdit.setReadOnly(True) 

    listOfObjects = [self.ui.lineEdit, self.ui.bt_submit, self.ui.lb_msg_success] 

    self.ui.bt_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    self.ui.bt_submit.clicked.connect(lambda: validate(self, task_to_generate, listOfObjects, scenario))

#########################################
## Method to add some attributes to UI elements
#########################################
def customUISetup(self):
      self.ui.setupUi(self)
      ## REMOVE WINDOW
      self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
      ## ADD EFFECTS
      self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      self.shadow = QGraphicsDropShadowEffect(self)
      self.shadow.setBlurRadius(50)
      self.shadow.setXOffset(0)
      self.shadow.setYOffset(0)
      self.shadow.setColor(QColor(0,92,157,550))
      self.ui.centralwidget.setGraphicsEffect(self.shadow)
      ## CHANGE TITLE AND ICON
      self.setWindowIcon(QtGui.QIcon(":/icons/icons8-system-information-50.png"))
      self.setWindowTitle("Validation System")

      ## CONNECT CLOSE AND MINIMIZE BUTTONS
      self.ui.bt_minimize_window.clicked.connect(lambda: self.showMinimized())
      self.ui.bt_close_window.clicked.connect(lambda: self.close())

#########################################
## Method to validate the solution
#########################################
def validate(self, validation, listOfObjects, scenario):
    answer = listOfObjects[0]
    button = listOfObjects[1]
    label = listOfObjects[2]
    
    response = getFlagcheck(self,scenario.id,validation.id,answer.text())
    print(response.status_code)
    if(response.status_code == 200):
        api_answer = response.json()
        if api_answer['answer'] == 'True' :
            validateSuccess(self, validation, answer, button, label, scenario)
        elif api_answer['answer'] == 'False' :
            label.setText(QCoreApplication.translate("MainWindow", u"Wrong!", None))
            label.setStyleSheet(u"color: rgb(255, 21, 21);")
        elif api_answer['answer'] != '' :
            # run the script
            result = runControllScript(self, api_answer['answer'], scenario.id, validation.id)
            print("Result from API: " + result)
            if result == 'True' :
            	validateSuccess(self, validation, answer, button, label, scenario)
            elif result == 'False' :
            	label.setText(QCoreApplication.translate("MainWindow", u"Wrong!", None))
            	label.setStyleSheet(u"color: rgb(255, 21, 21);")
 
def validateSuccess(self, validation, answer, button, label, scenario):
    # update components
    # Set success text + backgroud color to green, lock button and input field
    label.setStyleSheet(u"color: rgb(49, 255, 3);")
    label.setText(QCoreApplication.translate("MainWindow", u"Success", None))
    button.setStyleSheet(u"background-color: rgb(49, 255, 3);")
    
    # update progress bar and validation locally
    #scenario = updateProgressBar(self, scenario)
    #validation.completed = "true"
    scenario.calculateProgress(scenario.current, scenario.steps)
    updateProgressBar(self, scenario)

    disableUI(self)
    
#########################################
## Method to calculate current step
#########################################
def calculateCurrent(self,scenario):
    stepID = 10000000
    for step in scenario.validations:
        if step.completed == "false" and stepID > step.id:
            stepID = step.id
            scenario.current = step.id

def disableUI(self):
    # allow user to proceed to the next step
    self.ui.bt_next.setEnabled(True) 
    #lock button and input field
    self.ui.bt_submit.setEnabled(False)
    self.ui.lineEdit.setReadOnly(True)

def enableUI(self):
    #lock button and input field
    self.ui.bt_submit.setEnabled(True)
    self.ui.lineEdit.setReadOnly(False)
    
    
def updateProgressBar(self, scenario):
    #currently dummy solution
    if(scenario.id == 0):
        self.ui.progressBar_0.setValue(scenario.progress)
    if(scenario.id == 1):
        self.ui.progressBar_1.setValue(scenario.progress)
    if(scenario.id == 2):
        self.ui.progressBar_2.setValue(scenario.progress)
    if(scenario.id == 3):
        self.ui.progressBar_3.setValue(scenario.progress)
    if(scenario.id == 4):
        self.ui.progressBar_4.setValue(scenario.progress)
    if(scenario.id == 5):
        self.ui.progressBar_5.setValue(scenario.progress)
