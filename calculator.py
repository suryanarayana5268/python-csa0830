a=int(input('enter number:'))
b=int(input("enter number:"))
c=input("enter choice +,-,*,/:")
if c=='+':
    print("sum=",a+b)
elif c=='-':
    print("sub=",a-b)
elif c=='*':
    print("mul=",a*b)
elif c=="/":
    print("div=",a/b)
else:
    print("invalid command")