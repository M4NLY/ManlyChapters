from tkinter import *
from tkinter import ttk
from math import pi 

class Shape:
    def __init__(self):
        self.sides=[]
    
    def inputSides(self):
        pass
    
    def area(self):
        pass
    
class Circle(Shape):
    def inputSides(self):
        try:
            r = float(entry_radius.get())
            self.sides.append([r])
        except ValueError:
            area_result.set("Invalid numbers.")
    
    def area(self):
        if self.sides:
            return pi * self.sides[0][0] ** 2
        else:
            return 0
        
class Rectangle(Shape):
    def inputSides(self):
        try:
            l = float(entry_length.get())
            w = float(entry_width.get())
            self.sides.append([l, w])
            
        except ValueError:
            area_result.set("Invalid numbers.")
            
    def area(self):
        if len(self.sides) == 1:
            return self.sides[0][0] * self.sides[0][1]
        else:
            return 0

class Triangle(Shape):
    def inputSides(self):
        try:
            b = float(entry_base.get())
            h = float(entry_height.get())
            self.sides.append([b, h])
        
        except ValueError:
            area_result.set("Invalid Numbers.")
    
    def area(self):
        
        if len(self.sides) == 1:
            return 0.5 * self.sides[0][0] *self.sides[0][1]
        else:
            return 0

def calculate_area(shape):
    shape.inputSides()
    area_result.set(f"Area: {shape.area()}")

def shape_change(*args):
    selected_shape = shape_var.get()
    
    if selected_shape == "Circle":
        label_radius.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_radius.grid(row=1, column=1, padx=10, pady=5)
        
        label_length.grid_forget()
        entry_length.grid_forget()
        label_width.grid_forget()
        entry_width.grid_forget()
        label_base.grid_forget()
        entry_base.grid_forget()
        label_height.grid_forget()
        entry_height.grid_forget()
    
    elif selected_shape == "Rectangle":
        label_length.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_length.grid(row=1, column=1, padx=10, pady=5)
        label_width.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_width.grid(row=2, column=1, padx=10, pady=5)
        
        label_radius.grid_forget()
        entry_radius.grid_forget()
        label_base.grid_forget()
        entry_base.grid_forget()
        label_height.grid_forget()
        entry_height.grid_forget()
        
    elif selected_shape == "Triangle":
        label_base.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_base.grid(row=1, column=1, padx=10, pady=5)
        label_height.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        entry_height.grid(row=2, column=1, padx=10, pady=5)
        
        label_radius.grid_forget()
        entry_radius.grid_forget()
        label_length.grid_forget()
        entry_length.grid_forget()
        label_width.grid_forget()
        entry_width.grid_forget()
    
    area_result.set("")
        
        
#Create the main window
root = Tk()
root.title("Shape Area Calculator")

#Widgets
label_shape = Label(root, text="Select Shape:")
label_shape.grid(row=0, column=0, padx=10, pady=10, sticky="w")

shape_var = StringVar()
shape_var.set("Circle")

shapes = ["Circle", "Rectangle", "Triangle"]
dropdown_shape = OptionMenu(root, shape_var, *shapes)
dropdown_shape.grid(row=0, column=1, padx=10, pady=10)

label_radius = Label(root, text="Radius:")
label_length= Label(root, text="Length:")
label_width= Label(root, text="Width:")
label_base= Label(root, text="Base:")
label_height = Label(root, text="Height:")

entry_radius = Entry(root)
entry_length = Entry(root)
entry_width = Entry(root)
entry_base = Entry(root)
entry_height = Entry(root)

btn_calculate = Button(root, text="Calculate Area", command=lambda: calculate_area(shape_dict[shape_var.get()]))

area_result = StringVar()
label_result = Label(root, textvariable=area_result)

#Grid Layout

label_radius.grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_length.grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_width.grid(row=2, column=0, padx=10, pady=5, sticky="e")
label_base.grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_height.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_radius.grid(row=1, column=1, padx=10, pady=5)
entry_length.grid(row=1, column=1, padx=10, pady=5)
entry_width.grid(row=2, column=1, padx=10, pady=5)
entry_base.grid(row=1, column=1, padx=10, pady=5)
entry_height.grid(row=2, column=1, padx=10, pady=5)

dropdown_shape.grid(row=0, column=1, padx=10, pady=10)

btn_calculate.grid(row=3, column=0, columnspan=2, pady=10)

label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Create instances of shape classes
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

# Dictionary to map shape names to their corresponding class instances
shape_dict = {"Circle": circle, "Rectangle": rectangle, "Triangle": triangle}

# Set up trace on shape_var to call shape_changed whenever its value changes
shape_var.trace("w", shape_change)

# Start the Tkinter main loop
root.mainloop()



