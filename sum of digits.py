n=int(input("enter a number"))
num=int(input("enter digits:"))
sum=0
while num>0:
    a=num%10
    sum+=a
    num=num//10
print("sum of digits=",sum)