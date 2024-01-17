num = [10, 8, 7, 2, 9, 11, 15, 29, 24, 22]

#Print numbers using for loop
print("List of numbers using for loop: ")
for digit in num:
    print(digit)

#Get the highest and lowest number
max_num = max(num)
min_num = min(num)

print(f"\nThe highest number in the list is {max_num} and the lowest is {min_num}.")

#Arrange in ascending order
num.sort()
print(f"\nThe list arranged in ascending order: {num}")

#Arrange in descending order
num.sort(reverse=True)
print(f"\nThe list arranged in descending order: {num}")

#Append two numbers and update the list
num.append(26)
num.append(12)

print(f"\nThe updated list: {num}")