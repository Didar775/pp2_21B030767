def squares(n):
    i=1
    for _ in range(n):
        yield i**2
        i+=1

n=int(input())
it=squares(n)
print(*it)