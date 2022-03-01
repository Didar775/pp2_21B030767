from itertools import permutations

def Permutation(s):
  p=permutations(s)
  for i in p:
    for j in i:
        print(j,end="")
    print()

s=input()
Permutation(s)
