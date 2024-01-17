def print_pyramid(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

height = 5 
print_pyramid(height)
