n=input("enter statement")
vcount=0
ccount=0
for i in n:
    if i in("aeiou"):
        vcount+=1
    else:
        ccount+=1
print(vcount)
print(ccount)