#Program that can calculate the area of a square, triangle, or circle, depending on the user's choice.
while True:
    choice = input("What would you like to calculate for?: \n\n1. The area of a square \n2. The area of a circle \n3. The area of a triangle\n\nInput (1, 2, or 3): ")

    if choice in ["1", "2", "3"]:
        break
    else:
        print("\nInvalid choice. Please choose 1, 2, or 3.\n")

if choice == "1":
    a = int(input("\nEnter the length of the side of the square: "))
    area = a**2
    print(f"The area of the square is {area}.")
    
elif choice == "2":
    a = int(input("\nEnter the radius of the circle: "))
    area = a**2 * 3.14
    print(f"The area of the circle is {area}.")
    
elif choice == "3":
    a = int(input("\nEnter the base of the triangle: "))
    b = int(input("Enter the height of the triangle: "))
    area = b*a/2
    print(f"The area of the triangle is {area}.")



