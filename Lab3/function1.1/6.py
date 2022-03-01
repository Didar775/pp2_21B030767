def revers(s):
    s=s[::-1]
    return s

l=list(map(str,input().split()))
print(*revers(l))