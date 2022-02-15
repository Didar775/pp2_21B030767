def Puzzle(x,y):
    print("chickens:", int(2*x-y/2))
    print("rabbits:", int(y/2-35))
    
x,y=map(int,input().split())
Puzzle(x,y)