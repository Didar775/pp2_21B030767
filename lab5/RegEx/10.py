import re

REG = r"(.+?)([A-Z])"

def snake(match):
    return match.group().lower() + "_" + match.group().lower()
s=input()

print(re.sub(REG,snake,s))
