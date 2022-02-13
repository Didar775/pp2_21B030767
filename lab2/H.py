import math
x1,y1=map(int,input().split())
n=int(input())
arr_x=[]
arr_y=[]
arr_l=[]

for i in range(n):
    x2,y2=input().split()
    x2=int(x2)
    y2=int(y2)
    arr_x.append(x2)
    arr_y.append(y2)
    l=math.sqrt((x2-x1)**2+(y2-y1)**2)
    arr_l.append(l)
   
arr_l.sort()

for i in range(n):
    for j in range(n):
       a=math.sqrt((arr_x[j]-x1)**2+(arr_y[j]-y1)**2)
       if arr_l[i]==a:
          print(arr_x[j], arr_y[j])
         