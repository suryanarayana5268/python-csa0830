a=int(input("sub1 marks:"))
b=int(input("sub2 marks:"))
c=int(input("sub3 marks:"))
total=a+b+c
avg=total/3
print("total marks:",total)
print("avg marks:",avg)
if avg>=90:
    print("Grade A")
elif avg>=80 and avg<90:
    print("Grade B")
elif avg>=70 and avg<80:
    print("Grade c")
elif avg>=60 and avg<70:
    print("Grade D")
else:
    print("Grade F")