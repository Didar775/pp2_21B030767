import re
text=input()
l=re.findall(r'[A-Z][^A-Z]*',text)
print(*l)
