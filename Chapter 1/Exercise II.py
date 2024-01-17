digit = input("Input any number that has 2 or more digits: ")

digits = [int(d) for d in digit]

sum_digit = sum(digits)

print(f"\nThe total of the digits are {sum_digit}.")
