def division(n):
    i=0
    for _ in range(n):
        if i%3==0 and i%4==0:
            yield i  
        i+=1
    
n=int(input())
it=division(n)
print(*it)