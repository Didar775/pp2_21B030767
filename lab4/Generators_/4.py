def sqr_of_range(a,b):
    i=a
    for _ in range(b-a+1):

        yield i**2
        i+=1


a,b=map(int,input().split())
it=sqr_of_range(a,b)
print(*it)