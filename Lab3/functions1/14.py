def filter_prime(arr): #7 8 9
    cnt = 0
    l=[]
    for i in range(len(arr)):
        k=int(arr[i])
        if k==1:
            continue                    #FUNCTION FOR PRIME NUMBERS
        for j in range(2, k-1):       
            if k%j==0:
                cnt+=1
        if cnt == 0:
            l.append(k)
        cnt=0
    return l




from itertools import permutations
def print_permutation(s):
    p = permutations(s)                     #FUNCTION FOR PERMUTATIONS
    for i in p:
        for j in i:
            print(j,end='')
        print()
      
        
        
        
def reverse_sentences(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i], end=" ")              #FUNCTION FOR REVERSE
s = input().split()
reverse_sentences(s)




from enum import unique
def unique(arr):
    l = []
    for i in arr:                           #FUNCTION FOR UNIQUE
        if i not in l:
            l.append(i)
    return l




def check_palindrome(s): #qazaq
    ok = True
    k = len(s)-1 #4
    for i in range(int(len(s)/2)): #1       #FUNCTION FOR PALINDROME
        if s[i]!=s[k]:
            ok= False
            return ok
        k-=1
    return ok