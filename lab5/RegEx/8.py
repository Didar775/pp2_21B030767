import re
text=input()
l=[]
l=re.findall(r'[A-B][^A-B]*',text)
print(*l)
