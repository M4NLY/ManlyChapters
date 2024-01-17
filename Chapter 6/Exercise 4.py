import matplotlib.pyplot as plt

# Draw a line from (1, 2) to (6, 8)
x_values_line = [1, 6]
y_values_line = [2, 8]

# Draw a dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
x_values_dotted_line = [1, 2, 6, 8]
y_values_dotted_line = [3, 8, 1, 10]

plt.plot(x_values_line, y_values_line, label='Line', marker='o')
plt.plot(x_values_dotted_line, y_values_dotted_line, label='Dotted Line', linestyle='dotted', marker='x')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line and Dotted Line')

# Add legend
plt.legend()

# Display the plot
plt.show()
