import re

REG = r"(.*?)_([a-zA-Z])"

def camel(match):
    return match.group(1) + match.group(2).upper()

s=input()

results =re.sub(REG, camel, s)
print(results)