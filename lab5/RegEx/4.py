import re
text=input()
pattern=r"[A-Z][a-z]+"
if re.search(pattern,text):
    print("Correct")
else:
    print("Incorrect")