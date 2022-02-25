class Shape:
    def __init__(self):
        self.area=0

    def __Area(self):
        print(self.area)

class Square(Shape):
    def __init__(self,length):
        self.length=length
        self.area=0
    def Area(self):
        area=self.length**2
        print(area)
        
a=int(input())
Squ=Square(a)
Squ.Area()
