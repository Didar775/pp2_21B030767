def change_to_ounces(x):
    return x*28.3495231

n=int(input())
print(f"{n} gram={change_to_ounces(n)} ounces")