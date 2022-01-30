x,y=map(int,input().split())
ok=False
for i in range(2,x):
    if x%i==0 :
        ok=True
if ok==False and x<=500 and y%2==0:
    print("Good job!")
else:
    print("Try next time!")


