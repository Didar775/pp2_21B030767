from enum import unique


def unique(arr):
    l = []
    for i in arr:
        if i not in l:
            l.append(i)
    return l

l = input().split()
print(*unique(l))