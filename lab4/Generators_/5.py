def numbers(n):
    i=n
    for _ in range(n+1):
        yield i
        i-=1


n=int(input())
it=numbers(n)
print(*it)