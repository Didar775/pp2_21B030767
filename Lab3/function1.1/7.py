def next_3(arr):
    for i in range(len(arr)-1):
        if arr[i]==3 and arr[i+1]:
            return True
    return False

l=list(map(int,input().split()))
print(next_3(l))