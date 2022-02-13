n=int(input())
dict1={}
max=-1000000
for i in range(n):
    s,k=input().split()
    if s in dict1:
        dict1[s]+=int(k)
    else:
        dict1[s]=int(k)
    if max<dict1[s]:
        max=dict1[s]
arr=list(dict1.keys())
arr.sort()
for i in arr:
    if max==dict1[i]:
        print(i, "is lucky!")
    else:
        print(i, "has to receive", max-dict1[i], "tenge")
       
  
print(len(arr))