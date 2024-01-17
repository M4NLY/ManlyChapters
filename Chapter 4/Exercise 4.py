from tkinter import *
from tkinter import messagebox

def count_occurrences(character):
    try:
        with open('sentences.txt', 'r') as file:
            content = file.read()
        count = content.count(character)
        return count
    except FileNotFoundError:
        return None

def get_user_input():
    character = entry.get().lower()
    if len(character) == 1 and character.isalpha():
        occurrences = count_occurrences(character)
        if occurrences is not None:
            result_label.config(text=f"Occurrences of '{character}': {occurrences}")
        else:
            result_label.config(text="File not found: sentences.txt")
    else:
        messagebox.showerror("Error", "Please enter a single alphabetical character.")

# Create the main window
root = Tk()
root.title("Character Occurrence Counter")

# Create and set up widgets
instruction_label = Label(root, text="Enter a character:")
instruction_label.pack(pady=10)

entry = Entry(root, width=5)
entry.pack(pady=10)

count_button = Button(root, text="Count Occurrences", command=get_user_input)
count_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
