n=(2,4,5,6,7,8,9,1)
even=0
odd=0
for i in n:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("even number=",even)
print("odd number=",odd)