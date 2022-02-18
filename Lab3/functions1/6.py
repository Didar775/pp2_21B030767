def f(x):
    a=x[::-1]
    return a

s=list(map(str,input().split()))
print(*f(s))
