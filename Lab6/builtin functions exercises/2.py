def letter(s):
    cnt_u, cnt_l = 0, 0
    for i in s:
        if i.isupper():
            cnt_u+=1
        elif i.islower():
            cnt_l+=1
    print(f"Number of upper case: {cnt_u}")
    print(f"Nimber of lower case: {cnt_l}")

s = input()
letter(s)
