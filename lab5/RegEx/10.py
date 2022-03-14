import re

REG = r"(.+?)([A-Z])"

def snake(match):
    return match.group(1).lower() + "_" + match.group(2).lower()
s=input()

print(re.sub(REG,snake,s))
