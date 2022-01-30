s=input()
t=input()
if s.find(t)!=s.rfind(t) and s.count(t)==1:
     print(s.find(t),end=" ")
     print(s.rfind(t))
else:
    print(s.rfind(t))