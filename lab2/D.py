n=int(input())
if n%2==1:
   for i in range(n):
      for j in range(n-i-1):
          print('.',end="")
      for j in range(i+1):
          print('#',end="")
      print()
else:
    for i in range(n):
        for j in range(i+1):
            print('#',end="")
        for j in range(n-i-1):
            print('.',end="")
        print()




