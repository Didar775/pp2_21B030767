list1=[]
sum=0
arr=list(map(int,input().split()))
if len(arr)==2:
    for i in range(arr[0]):
     list1.append(arr[1]+2*i)
    for i in range(arr[0]):
      sum^=list1[i]
    print(sum)
else:
    y=int(input())
    for i in range(arr[0]):
     list1.append(y+2*i)
    for i in range(arr[0]):
        sum^=list1[i]
    print(sum) 