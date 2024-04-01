a=input("enter string")
st=list(a)
for i in range(len(st)):
     for j in range(len(st)-i-1):
         if st[j]<st[j+1]:
             t=st[j]
             st[j]=st[j+1]
             st[j+1]=t
print(''.join(st))