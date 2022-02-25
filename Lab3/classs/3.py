class Shape:
    def __init__(self):
        self.area=0
    def Area(self):
        print(self.area)

class Restangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.area=0
    def Area(self):
        area=self.length*self.width
        print(area)
        
a,b=map(int,input().split())
S=Restangle(a,b)
S.Area()