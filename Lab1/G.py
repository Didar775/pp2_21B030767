s=input()
sum=0
n=len(s)-1
for i in range(len(s)):
    sum+=int(s[i])*(2**(n-i))

print(sum)    

