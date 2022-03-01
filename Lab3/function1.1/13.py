import random
print("Hello! What is your name?")
s=input()
print(f"Well, {s}, I am thinking of a number between 1 and 20.")
print("Take a guess")
k=random.randrange(1,20)

x=-1
cnt=0
while x!=k:
    n=int(input())
    if n<k:
        print("Your guess is too low ")
        print("Take a guess")
    elif n>k:
        print("Your guess too upper")
        print("Take a guess")
    else:
        print(f"Good job, {s}! You guessed my number in {cnt} guesses")
    cnt+=1
    x=n                              



