import re
s=input()
print(re.search(r'ab{2,3}$',s))