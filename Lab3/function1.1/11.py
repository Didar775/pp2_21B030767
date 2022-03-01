def palindrome(x):
    
    s=""
    for i in range(int(len(x))-1,-1,-1):
        s+=x[i]
    if s==x :
        return x ,"is palindrome"
        
    return x,"is not palindrome"
        
        
l=list(map(str,input().split()))
for i in l:
    print(*palindrome(i))