import os
path=input()
if os.path.exists(path):
    print(f"Directory: {os.path.dirname(path)}")
    print(f"Filename: {os.path.basename(path)}")
    with open(path,'r') as f:
        ff=f.readlines()
    print(*ff)
else:
    print('File not exist')

