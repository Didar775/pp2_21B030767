class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def show(self):
        print(f"coordinates of point:{self.x}:{self.y}")
        
    def move(self,x2,y2):
        self.x,self.y=x2,y2
    def dist(self):
        d=((self.y-self.x)**2+(self.x-self.y)**2)**(1/2)
        print(d)
        

p=Point(4,5)
print(p.dist())
