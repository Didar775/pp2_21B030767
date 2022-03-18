def Multiplication(l):
    cnt = 1
    for i in range(len(l)):
        cnt *= l[i]
    print(cnt)


l = list(map(int, input().split()))
Multiplication(l)
