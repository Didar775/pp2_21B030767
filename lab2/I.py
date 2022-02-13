n=int(input())
arr=[]
disc_p=[]
disc_t=[]

for i in range(n):
    arr=list(input().split())
    if len(arr)==2:
       disc_p.append(arr[1])
    elif len(disc_p)>0 and len(arr)==1:
        x=disc_p.pop(0)
        disc_t.append(x)

for i in disc_t:
    print(i,end=" ")
  

    
