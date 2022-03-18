import os

new_file = input("Enter name of file: ")
l = list(map(str, input().split()))
os.chdir(r'Lab6\Python Directories and Files exercises\Practise.example')
file=open(new_file,'w')
for word in l:
    file.write(word+'\n')


file.close()
