l=[]
x=-1
while(x!=0):
    s =input().split(' ')
    if int(s[0])==0:
        x=0
    else:
        l.append(s)
l.sort(key = lambda x: (x[2], x[1], x[0]))
for i in l:
    print(*i)