import Flow
import os
from colorama import Fore, Back, Style
class Debate:
  def __init__(self):
    self.contentions = []
    self.pointer = [0,0,1]
  
  def newContention(self, name):
    self.contentions.append(Flow.Contention(len(self.contentions),name))
  
  def print(self):
    os.system("cls")
    print(f"pointer: {self.pointer}")
    for contention in self.contentions:
      contention.printContention()
  
  def extractText(self,thing:list):
    text = ""
    for i in range(2,len(thing)):
      text += thing[i] + " "
    return text
  
  def throwError(self, err:str):
    self.print()
    print(Fore.RED+err)

  def parse(self, cmd:str):
    if cmd == "exit":
      return False
    
    elif "switch" in cmd:
      thing = cmd.split(" ")
      np = thing[1].split(".")
      if len(np)>=1:
        self.pointer[0] = int(np[0])
      if len(np)>=2:
        self.pointer[1] = int(np[1])
      
    elif "new" in cmd:
      thing = cmd.split(" ")
      text = self.extractText(thing)

      if thing[1]=="contention" or thing[1] == "c":
        self.newContention(text)
      
      elif thing[1]=="point" or thing[1]=="p":
        try:
          self.contentions[self.pointer[0]].newPoint(text)
        except:
          self.throwError("Err: the pointer is not pointing to a valid point.")
          return True

      elif thing[1]=="warrant" or thing[1]=="w":
        try:
          self.contentions[self.pointer[0]].addWarrant(self.pointer[1],text)
        except:
          self.throwError("Err: the pointer is not pointing to a valid point.")
          return True
    
      elif thing[1]=="impact" or thing[1]=="i":
        try:
          self.contentions[self.pointer[0]].addImpact(self.pointer[1],text)
        except:
          self.throwError("Err: the pointer is not pointing to a valid point.")
          return True

    self.print()   
    return True

    
