def prod(list):
    product = 1
    
    for num in list:
        product *= num
    
    return product

list = []

while True:
    add = input("Add numbers to the list. (Type 'DONE' if done.): ")

    if add.upper() == "DONE":
        print(f"\nThis is the list you made: {list}")
        break
    else:
        num = int(add)
        list.append(num)

result = prod(list)
print(f"\nThe product of all the numbers in the list is {result}.")

