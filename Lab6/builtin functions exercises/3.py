def palindrome(s):
    t=s[::-1]
    if t==s:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")

s=input()
palindrome(s)