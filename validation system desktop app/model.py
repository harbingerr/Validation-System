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
  progress = 0
  validations = []
  
  def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
  
  def calculateProgress(self, progress, steps):
      if(progress == 0):
        self.progress = 0
      else:
        self.progress = (progress / steps) * 100

  def __init__(self, title, validations, id, progress, steps):  
      self.title = title
      self.validations = validations
      self.id = id
      if(progress == 0):
        self.progress = 0
      else:
        self.progress = (progress / steps) * 100
      
      self.steps = steps
      self.current = 1 + progress

#########################################
## Validation Model
#########################################
class Validation():
  task = ""
  type = ""
  completed = False

  def __init__(self, task, type, completed, stepNumber, hint, score):  
      self.task = task
      self.type = type
      self.completed = completed
      self.id = stepNumber
      self.hint = hint
      self.score = score