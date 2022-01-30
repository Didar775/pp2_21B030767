l=input()
s = []
k = l.count(" ") + 1
for i in range(k):
    c = input()
    s.append(c)


for i in range(len(s)):
    if len(s[i]) >= 3:
        print(s[i],end=" ")