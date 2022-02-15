def filter_prime(arr):
    
    for i in range(len(arr)):
      if arr[i]>1:
        for j in range(2,arr[i]):
            if arr[i]%j==0:
               break
         
        else:
            print(arr[i],end=" ")


arr=list(map(int,input().split()))
filter_prime(arr)

