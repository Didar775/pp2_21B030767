import os
path=input()
if os.path.exists(path):
    print('Path exist')
else:
    print('Path not exist')
try:
    os.remove(path)
except Exception:
    pass