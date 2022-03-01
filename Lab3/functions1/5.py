from itertools import permutations

def perm(x):
    p=permutations(x)
    for i in p:
        for j in i:
            print(j,end="")
        print()

    

s=input()
print(perm(s))
