num1={"ONE":"1","TWO":"2","THR":"3","FOU":"4","FIV":"5",
"SIX":"6","SEV":"7","EIG":"8","NIN":"9","ZER":"0"}

num2={"1":"ONE","2":"TWO","3":"THR","4":"FOU","5":"FIV",
"6":"SIX","7":"SEV","8":"EIG","9":"NIN","0":"ZER"}

sum=0

def f(x):
 dig=""
 letter=""
 for i in range(len(x)):
       if i == len(x)-1:
           letter+=x[len(x)-1]
       if len(letter)!=3:
          letter+=x[i]
       else:
           if letter in num1.keys():#ONETWO
            dig+=num1[letter]
            letter=x[i]
 return dig

s=input().split("+") 
for i in s:
    sum+=int(f(i))
    
sum=str(sum)
for i in sum:
    if i in num2:
        print(num2[i],end="")




