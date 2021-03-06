#########################################
## LIB IMPORTS
#########################################
from calendar import c
from functools import cache
import json
import requests
import sys
import os
from turtle import width
from PySide2 import *
from scipy.fftpack import fftfreq

#########################################
## FILE IMPORTS
#########################################
from ui_untitled_demo import *
from model import *
from view import *
from controller import *
from constants import *

#########################################
#########################################
## CONTROL
#########################################
#########################################

#########################################
## Method to run the controll script
#########################################
def runControllScript(self, script, scenarioId, validationId):
  if os.name == 'posix':
    stream = os.popen(script)
    output = stream.read()
    print(output)
    finalResult = sendOutput(self,str(output), scenarioId, validationId)
    if(finalResult.status_code == 200):
        api_answer = finalResult.json()
        return api_answer['answer']
  else:
    print('You are running this system on windows machine')
    output = "False"
    return output

#########################################
## Method to check output from script
#########################################
def sendOutput(self, output, scenarioId, validationId):    
  query = {'scenario':scenarioId, 'validation':validationId, 'output':output}    
  return requests.get(API_SOURCE+API_ENDPOINT_INIT+'/'+API_ENDPOINT_VALIDATE2, params=query)

#########################################
## Method to generate scenario widget
#########################################
def generateScenarios(self):
  for scenario in extractedData:
    generateCards2(self,scenario)
    
#########################################
## Method to get init informations from API
#########################################
def getInfo(self):
  try:
    r = requests.get(API_SOURCE+API_ENDPOINT_INIT)
    return r
  except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
  except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
  except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)  
  return None
  

#########################################
## Method to check flag
#########################################
def getFlagcheck(self, scenarioId, validationId, answer):    
  query = {'scenario':scenarioId, 'validation':validationId, 'flag':answer}    
  return requests.get(API_SOURCE+API_ENDPOINT_INIT+'/'+API_ENDPOINT_VALIDATE, params=query)

#########################################
## Method to get init informations from API
#########################################
def postSomething(self):
  return requests.get(API_SOURCE+API_ENDPOINT_INIT)

#########################################
## Method to extract Scenarios from JSON
#########################################
def extractScenarios(initData):
  ## List of scenarios
  scenarios = []
  for scenario in initData["scenarios"]:
      ## List of validations
      validations = []   
      for validation in scenario["validations"]:
            validations.append(Validation(validation["task"],validation["type"],validation["completed"],validation["step"]))
      scenarios.append(Scenario(scenario["title"],scenario["desc"],validations,scenario["id"],scenario["progress"],scenario["steps"]))
  
  return scenarios

#########################################
## MAIN CLASS
#########################################
class MainWindow(QMainWindow):
  def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        customUISetup(self)
        response = getInfo(self)
        if response != None:
          #response = requests.get("http://192.168.1.106:4999/attacker")
          print(response.json())
                
          global extractedData
          extractedData = extractScenarios(response.json())

          ## Generate cards for scenarios
          generateScenarios(self)

        def moveWindow(e):
          if(e.buttons() == Qt.LeftButton):
            self.move(self.pos() + e.globalPos() - self.clickPosition)
            self.clickPosition = e.globalPos()
            e.accept()

        self.ui.header.mouseMoveEvent = moveWindow
        self.show()
  
  def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        

        

#########################################
## EXECUTE APP
#########################################
if __name__ == "__main__":
      app = QApplication(sys.argv)
      window = MainWindow()
      sys.exit(app.exec_())