s=input()
cnt1=0
cnt2=0
for i in range(len(s)):
    if s[i]!=" ":
       cnt1=cnt1+1 
       if cnt1>=3:
        for j in range(cnt1):
           print(s[j])
    cnt1=0

# I am fine and what about u?