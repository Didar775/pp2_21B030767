def fib(arr):
    for i in range(len(arr)-1):
        if arr[i]==3 and arr[i+1]==3:
            return "True"
    
    return "False"


l=list(map(int,input().split()))
print(fib(l))