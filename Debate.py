import Flow
class Debate:
  def __init__(self):
    self.contentions = []
    self.pointer = [0,0,1]
  
  def newContention(self, name):
    self.contentions.append(Flow.contention(len(self.contentions)),name)
  
  def parse(self, cmd:str):
    if cmd == "exit":
      return False
    elif "switch" in cmd:
      thing = cmd.split(" ")
      np = thing[1].split(".")
      pointer[0] = np[0]
      
    elif "new" in cmd:
      thing = cmd.split(" ")
      if thing[1]=="contention" or thing[1] == "c":
        newContention(thing[2])
      elif thing[1]=="point" or thing[1]=="p":
        self.contentions[self.pointer[0]].newPoint(thing[2])
      elif thing[1]=="warrant" or thing[1]=="w":
        self.contentions[self.pointer[0]].addWarrant(self.pointer[1],thing[2])
        
        

    
