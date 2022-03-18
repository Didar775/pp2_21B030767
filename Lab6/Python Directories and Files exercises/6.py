import os
os.chdir(r'Lab6\Python Directories and Files exercises\Practise.example')
for i in range(65,91):
    open(f"{chr(i)}.txt","r")

# for i in range(65,91):
#     os.remove(f"{chr(i)}.txt")