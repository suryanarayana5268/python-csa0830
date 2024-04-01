n=int(input("enter no of elements:"))
li=[]
a=[]
for i in range(n):
    num=int(input("enter elements"))
    a.append(num)
evensum=0
oddsum=0
for i in range(n):
    if a[i]%2==0:
        evensum+=a[i]**2
    else:
        oddsum+=a[i]**2
li.append(evensum)
li.append(oddsum)
print(li)
