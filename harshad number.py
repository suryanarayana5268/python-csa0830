n=int(input())
p=n
sum=0
while(n>0):
    sum+=n%10
    n=n//10
if(p%sum==0):
    print("harshad number")
else:
    print("not harshad number")