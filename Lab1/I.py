n=int(input())
arr=[]
for i in range(n):
    s=input()
    arr.append(s)

for i in range(n):
    if arr[i].find("@gmail.com")>0:
        print(arr[i].replace('@gmail.com',""))
