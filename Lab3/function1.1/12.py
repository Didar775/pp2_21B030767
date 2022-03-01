def histogram(s):
    for i in s:
        for j in range(i):
            print("*",end="")
        print()



l=[int(i) for i in input().split()]
histogram(l)