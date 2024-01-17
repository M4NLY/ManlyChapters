side1 = int(input("\nEnter the length of the 1st side: "))
side2 = int(input("\nEnter the length of the 2nd side: "))
side3 = int(input("\nEnter the length of the 3rd side: "))

if  side3 > side1 + side2:
    print("\nThis is not a valid triangle!")
    
elif side3 <= side1 + side2:
    print("\nThis is a valid triangle!")


if side1 == side2 == side3:
    print("\nThis is an equilateral triangle!")
    
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("\nThis is an isosceles triangle!")

else:
    print("\nThis is a scalene triangle!")

