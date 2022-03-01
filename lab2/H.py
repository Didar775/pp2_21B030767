def rak(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**1 / 2


x1, y1 = list(map(int, input().split()))
n = int(input())
arr = []
for _ in range(n):
    x2, y2 = map(int, input().split())
    a = rak(x1, x2, y1, y2)
    arr.append((x2, y2, a))
for x2, y2, a in sorted(arr, key=lambda x: (x[2])):
    print(x2, y2)
