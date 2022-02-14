n=int(input())
dem={}
for i in range(n):
    d,w=input().split()
  
    if w in dem:
         dem[w]+=1
    else:
         dem[w]=1

k=int(input())
hun={}
kill=0
    
for i in range(k):
    h,a,f=input().split()
    if a in hun:
      hun[a]+=int(f)
    else:
      hun[a]=int(f)

for i in dem:
    for j in hun:
        if i==j and hun[j]-dem[i]>=0:
            n-=dem[i]
        elif i==j and hun[j]-dem[i]<0:
            n-=hun[j]

print("Demons left:", n)