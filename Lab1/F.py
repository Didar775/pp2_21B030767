n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

for i in range(n):
    if arr[i] <= 10:
        print("Go to work!")
    elif arr[i] > 10 and arr[i] <= 25:
        print("You are weak")
    elif arr[i] > 25 and arr[i] <= 45:
        print("Okay, fine")
    elif arr[i] > 45:
        print("Burn! Burn! Burn Young!")
