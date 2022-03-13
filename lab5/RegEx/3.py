import re
# def text_match(text):
#         patterns = r'[a-z][_][a-z]'
#         if re.search(patterns, text):
#                 return 'Found a match!'
#         else:
#                 return('Not matched!')

s = input()
# print(text_match(s))
print(re.search(r'[a-z][_][a-z]',s))