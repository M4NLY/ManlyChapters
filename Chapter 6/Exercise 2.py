a = [20, 23, 82, 40, 32, 15, 67, 52]

# Task 1: Find the indices of even numbers
even_indices = [index for index, value in enumerate(a) if value % 2 == 0]
print("Indices of even numbers:", even_indices)

# Task 2: Sort the array
sorted_array = sorted(a)
print("Sorted array:", sorted_array)

# Task 3: Slice elements from index 3 to the end of the array
slice_from_3 = a[3:]
print("Slice from index 3 to the end:", slice_from_3)

# Task 4: Slice elements from index 0 to index 4
slice_from_0_to_4 = a[0:5]
print("Slice from index 0 to index 4:", slice_from_0_to_4)

# Task 5: Print [32, 15, 67] using negative slicing
negative_slice_result = a[-5:-2]
print("Using negative slicing to print [32, 15, 67]:", negative_slice_result)
