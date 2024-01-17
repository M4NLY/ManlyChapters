name = input("Hello, user! \nEnter your name: ")
age = int(input("Please enter your age: "))

print(f"\nIt's nice to meet you, {name.title()}!") #capitalizes the first letter of the name
print(f"\nYour name is {len(name)} characters long.")

age += 1 #increment of one 

print(f"\nYou'll be {age} next year!")

