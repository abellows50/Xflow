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
    elif "new" in cmd:
      thing = cmd.split(" ")
      if thing[1]=="contention" or thing[1] == "c":
        newContention(thing[2])
        

    
