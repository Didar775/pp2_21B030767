def spy_game(s):
    t=""
    for i in s:
        if i=='7' or i=='0':
          t+=i

    if t.find("007")>=0:
        return True
    return False

s =[str(i) for i in input().split()]
print(spy_game(s))