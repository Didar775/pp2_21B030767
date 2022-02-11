n=int(input())
dem=[]
for i in range(n):
    dem.append(input().split())

m=int(input())
hun=[]
for i in range(m):
    hun.append(input().split())
count=0
size=0
for i in range(m):
     for j in range(n):
        count=0
        if dem[j][1]==hun[i][1]:
            count+=1
        size+=count
        if count<int(hun[i][2]) and n>size:
          n-=size

print("Demons left:",end=" ")
print(n)



           

