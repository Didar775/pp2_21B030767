s=input()

b={"(":")","{":"}","[":"]"}
l=[]
cnt=0
for i in s:
    if i in b.keys():
        l.append(i)
        cnt+=1
    else:
        if l:
            top=l.pop()

            if b[top]==i:
                cnt=0
if cnt==0 and len(l)==0:
    print("Yes")
else:
    print("No")






#        if i in b.values(): 
#            l.append(i)

#        elif (len(l)>0) and (i in b.keys()) and (b[i] in l) and (b[i] == l[len(l) - 1]):
        
#            l.remove(b[i])
#        elif b[i] not in l:
#            l.append(i)
        
#  if len(l)==0:
#     print("Yes")
#  else:
#     print('No')

