n=int(input())
p=[]

for i in range(n):
   cnt_l=0
   cnt_u=0
   cnt_d=0
   x=input()

   for j in range(len(x)):
        if (x[j].islower()):
            cnt_l+=1
        elif (x[j].isupper()):
            cnt_u+=1
        else:
            cnt_d+=1
   if cnt_l>0 and cnt_u>0 and cnt_d>0:
       if x not in p:
        p.append(x)
p.sort()
print(len(p))

for x in p:
    print(x)