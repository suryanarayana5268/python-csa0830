n=int(input("enter number:"))
for i in range(n):
    for j in range(n):
        if(i==0 and j!=0 and j!=n-1):
            print("*",end=" ")