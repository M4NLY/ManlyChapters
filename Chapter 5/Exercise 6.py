from tkinter import *
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def calculate(self, operation, num1, num2):
        if operation == "Addition":
            self.result = num1 + num2
        elif operation == "Subtraction":
            self.result = num1 - num2
        elif operation == "Multiplication":
            self.result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                self.result = num1 / num2
            else:
                return "Error: Division by zero"
        return f"Result: {self.result}"

def perform_calculation():
    operation = operation_var.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    result_text.set(arithmetic.calculate(operation, num1, num2))

# Create the main application window
app = Tk()
app.title("Arithmetic Operations")

# Create an instance of the ArithmeticOperations class
arithmetic = ArithmeticOperations()

# Create widgets
label_num1 = Label(app, text="Number 1:")
label_num2 = Label(app, text="Number 2:")
label_operation = Label(app, text="Operation:")
label_result = Label(app, text="Result:")

entry_num1 = Entry(app)
entry_num2 = Entry(app)

operation_var = StringVar()
operation_var.set("Addition")

operation_combobox = ttk.Combobox(app, textvariable=operation_var, values=["Addition", "Subtraction", "Multiplication", "Division"])

result_text = StringVar()
result_label = Label(app, textvariable=result_text)

btn_calculate = Button(app, text="Calculate", command=perform_calculation)

# Arrange widgets in a grid
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_operation.grid(row=2, column=0, padx=10, pady=5, sticky="e")
label_result.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_num1.grid(row=0, column=1, padx=10, pady=5)
entry_num2.grid(row=1, column=1, padx=10, pady=5)
operation_combobox.grid(row=2, column=1, padx=10, pady=5)

btn_calculate.grid(row=4, column=0, columnspan=2, pady=10)

result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
app.mainloop()
