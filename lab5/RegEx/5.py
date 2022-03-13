import re
text=input()
pattern=r"^a.+b$"
if re.search(pattern,text):
    print('matched')
else:
    print('not matched')