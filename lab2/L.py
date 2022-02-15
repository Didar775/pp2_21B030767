s=input()

b={"(":")","{":"}","[":"]"}
if s[0] in b.values():
    print("No")
    exit()
   
l=[]
for i in s:
    if i in b.keys():
        l.append(i)
    
    else:
        if  l:
            top=l[len(l)-1]

            if b[top]==i:
                l.pop()
if  len(l)==0:
    print("Yes")
else:
    print("No")
    