from tkinter import *

def read_numbers_from_file():
    try:
        with open('numbers.txt', 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        return None

def show_numbers():
    numbers = read_numbers_from_file()
    if numbers is not None:
        result_text.set("\n".join(map(str, numbers)))
    else:
        result_text.set("File not found: numbers.txt")

# Create the main window
root = Tk()
root.title("Numbers Viewer")

# Create and set up widgets
result_text = StringVar()
result_label = Label(root, textvariable=result_text, justify=LEFT)
result_label.pack(padx=10, pady=10)

show_numbers_button = Button(root, text="Show Numbers", command=show_numbers)
show_numbers_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
