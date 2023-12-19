from colorama import Fore, Back, Style
class Contention:
    def __init__(self, id, title):
        self.title = "Contention"
        self.points = []
        self.id = id
        self.title = title

    def newPoint(self, pointHeader:str):
        point = Point(len(self.points),pointHeader)
        self.points.append(point)
    
    def addWarrant(self, pointId:int, warrant:str):
        self.points[pointId].addWarrant(warrant)
    
    def addImpact(self, pointId:int, impact:str):
        self.points[pointId].addImpact(impact)
    
    def printContention(self):
        print(Fore.WHITE + f"Contention {self.id}: {self.title}")
        for point in self.points:
            point.printPoint()

class Point:
    def __init__(self, id:int, header):
        self.id = 1
        self.header = "Point"
        self.content = ""
        self.warrants = []
        self.rebuttals = []
        self.impacts = []
        self.id = id
        self.header = header

    def addWarrant(self, content:str):
        self.warrants.append(content)
    
    def addImpact(self, content:str):
        self.impacts.append(content)
    
    def printPoint(self):
        print(Fore.GREEN + f"    Point {self.id}: {self.header}")
        for warrant in self.warrants:
            print(Fore.BLUE + f"        Warrant: {warrant}")
        for impact in self.impacts:
            print(Fore.YELLOW + f"        Impact: {impact}")
