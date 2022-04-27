#########################################
#########################################
## MODEL
#########################################
#########################################
import json

#########################################
## Scenario Model
#########################################
class Scenario():
  id = 0
  title = ""
  description = ""
  progress = 0
  validations = []
  
  def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
  
  def calculateProgress(self, progress, steps):
      print("Progress:" + str(progress))
      print("steps:" + str(steps))
      if(progress == 0):
        self.progress = 0
      else:
        self.progress = (progress / steps) * 100
      print("Progress after:" + str(self.progress))

  def __init__(self, title, description, validations, id, progress, steps):  
      self.title = title
      self.description = description
      self.validations = validations
      self.id = id
      print("Progress:" + str(progress))
      print("steps:" + str(steps))
      if(progress == 0):
        self.progress = 0
      else:
        self.progress = (progress / steps) * 100
      print("Progress after:" + str(self.progress))
      
      self.steps = steps
      self.current = 1 + progress

#########################################
## Validation Model
#########################################
class Validation():
  task = ""
  type = ""
  completed = False

  def __init__(self, task, type, completed, stepNumber):  
      self.task = task
      self.type = type
      self.completed = completed
      self.id = stepNumber