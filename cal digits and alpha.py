n=(input("enter a string:"))
alpha=0
digit=0
for i in n:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
print("letters=",alpha)
print("digits=",digit)