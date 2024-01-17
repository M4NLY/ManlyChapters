a = int(input("\nEnter your first number: "))
b = int(input("\nEnter your second number: "))
c = int(input("\nEnter your third number: "))

if a > b and a > c:
    print(f"{a} is the largest number out of the three numbers.")
    
elif b > a and b > c:
    print(f"{b} is the largest number out of the three numbers.")

else:
    print(f"{c} is the largest number out of the three numbers.")