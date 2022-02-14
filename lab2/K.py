s=list(map(str,input().split()))
punct=[',','!','.','?']
l=set()
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] in punct:
            s[i]=s[i].replace(s[i][j],"")

for i in s:
    l.add(i)
s=list(l)
s.sort()
print(len(s))
for x in s:
  print(x)