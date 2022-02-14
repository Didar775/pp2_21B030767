
s=list(map(str,input().split("+")))

num={"ONE":1,"TWO":2, "THR":3, "FOU":4,"FIV":5,
   "SIX":6,"SEV":7,"EIG":8,"NIN":9,"ZER":0}
arr1=list(num.keys())
arr2=list(num.values())
sum=""
num1=""

for x in s: 
    dig=""
    for i in range(len(x)):

        if len(dig)%3==0:
           for k in range(len(arr1)):
               if dig==arr1[k]:
                num1+=arr2[k]
           dig=""     
        else:
            dig+=x[i]
        
    sum+=num1       
        
print(sum)



         





