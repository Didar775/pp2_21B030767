def even_numbers(n):
    i=0
    for _ in range(n+1):
        if i%2==0:
             yield i
             
        i+=1
n=int(input())
it=even_numbers(n)
print(*it,sep=', ')


# cnt=0
# n=int(input())
# for i in even_numbers(n):
#     print(i,end="")
#     cnt+=1
#     if cnt<=n/2:
#         print(',',end="")




