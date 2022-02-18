def histogram(l):
    for i in range(len(l)):
        for j in range(l[i]):
            print('*', end = "")
        print()

arr = list(map(int,input().split()))
histogram(arr)