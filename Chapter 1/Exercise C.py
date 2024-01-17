choice = input("\n Welcome to the BSU Calculator!\n\nPlease choose the operation to perform: \n\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division\n5. Modulus Division\n\nInput (1, 2, 3, 4, or 5): ")

while True:
    if choice in ["1", "2", "3", "4", "5"]:
        break
    else:
        print("\nInvalid choice. Please choose 1, 2, 3, 4, or 5.\n")
        
if choice == "1":

    while True: 
        a = float(input("\nEnter the first number to add: "))
        b = float(input("Enter the second number to add: "))
    
        c = a + b

        print(f"The result is {c}.")
    
        con = input("Do you want to continue? (y/n): ")
    
        if con.lower() != "y":
            break
        
if choice == "2":

    while True: 
        a = float(input("\nEnter the first number to subtract: "))
        b = float(input("Enter the second number to subtract: "))
    
        c = a - b

        print(f"The result is {c}.")
    
        con = input("Do you want to continue? (y/n): ")
    
        if con.lower() != "y":
            break

if choice == "3":

    while True: 
        a = float(input("\nEnter the first number to multiply: "))
        b = float(input("Enter the second number to multiply: "))
    
        c = a * b

        print(f"The result is {c}.")
    
        con = input("Do you want to continue? (y/n): ")
    
        if con.lower() != "y":
            break

if choice == "4":

    while True: 
        a = float(input("\nEnter the first number to divide: "))
        b = float(input("Enter the second number to divide: "))
    
        c = a / b

        print(f"The result is {c}.")
    
        con = input("Do you want to continue? (y/n): ")
    
        if con.lower() != "y":
            break

if choice == "5":

    while True: 
        a = float(input("\nEnter the first number to perform modulus division on: "))
        b = float(input("Enter the second number to perform modulus division on: "))
    
        c = a % b

        print(f"The result is {c}.")
    
        con = input("Do you want to continue? (y/n): ")
    
        if con.lower() != "y":
            break

