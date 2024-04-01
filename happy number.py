n=int(input("Enter a number: "))
for i in range (n):
    n = sum(int(digit)** 2 for digit in str(n))
    if n == 1:
        print("It's a happy number!")
        break
else:
    print("It's not a happy number.")
