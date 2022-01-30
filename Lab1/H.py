s=input()
t=input()
cnt=0
for i in range(len(s)):
    if s[i]==t:
       cnt=cnt+1

if s.find(t)!=s.rfind(t) and cnt>1:
     print(s.find(t),end=" ")
     print(s.rfind(t))
else:
    print(s.rfind(t))