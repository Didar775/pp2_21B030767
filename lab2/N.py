n = -1
list = []
while n != 0:
    k = int(input())
    list.append(k)
    n = k
if int(len(list)) % 2 == 1:
    for i in range(int(len(list) / 2)):
        print(list[i] + list[len(list) - i - 2], end=" ")
else:
    for i in range(int(len(list) / 2 - 1)):
        print(list[i] + list[len(list) - i - 2], end=" ")
    print(list[int(len(list) / 2 - 1)])
