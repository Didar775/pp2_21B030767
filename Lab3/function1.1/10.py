def unique_e(arr):
    l=[]
    for i in arr:
        if i not in l:
            l.append(i)
    return l

arr=[int(i) for i in input().split()]
print(*unique_e(arr))
