from tkinter import *
from tkinter import ttk

#functions for cicles
def calc_circle_area(radius):
    radius = int(radius)
    area = radius **2 * 3.14
    return area

def circle_area_display():
    circle_area.config(text= f"The area of the circle is {calc_circle_area(radius.get())}")
    
#functions for squares

def calc_square_area(side):
    side = int(side)
    area = side **2 
    return area

def square_area_display():
    square_area.config(text= f"The area of the square is {calc_square_area(side.get())}.")
    

#functions for rectangles

def calc_rect_area(w,l):
    w = int(w)
    l = int(l)
    area = w * l
    return area

def rect_area_display():
    rectangle_area.config(text= f"The area of the rectangle is {calc_rect_area(w.get(), l.get())}.")

root = Tk()
root.title("Area Function")
root.geometry("300x200")

#Create the tabs

ntbk = ttk.Notebook(root)
ntbk.pack(pady=15)

#frames

f1 = Frame(ntbk)
f2 = Frame(ntbk)
f3 = Frame(ntbk)

#Add the frames to the notebook

ntbk.add(f1, text="Circle")
ntbk.add(f2, text="Square")
ntbk.add(f3, text="Rectangle")

#Circle

circle_title = Label(f1, text="Circle Area Calculator", font=("Arial", 15, "bold"))
circle_title.grid(column=1, row=0)

radius_label = Label(f1, text="Radius", font=("Arial", 10))
radius_label.grid(row=1, column=0)

radius = IntVar()

radius = Entry(f1, textvariable= radius)
radius.grid(row=1, column=1, pady=5)

circle_area = Label(f1, text="", font=("Arial", 10))
circle_area.grid(row=2, column=1, columnspan=2)

circle_button = Button(f1, text="Calculate", command=circle_area_display)
circle_button.grid(row=3, column=1, pady=5)

#Square

square_title = Label(f2, text="Square Area Calculator", font=("Arial", 15, "bold"))
square_title.grid(column=1, row=0)

side_label = Label(f2, text="Side", font=("Arial", 10))
side_label.grid(row=1, column=0)

side = IntVar()

side = Entry(f2, textvariable= side)
side.grid(row=1, column=1, pady=5)

square_area = Label(f2, text="", font=("Arial", 10))
square_area.grid(row=2, column=1, columnspan=2)

square_button = Button(f2, text="Calculate", command=square_area_display)
square_button.grid(row=3, column=1, pady=5)

#Rectnagles

rectangle_title = Label(f3, text="Rectangle Area Calculator", font=("Arial", 15, "bold"))
rectangle_title.grid(column=0, row=0, columnspan=2)

width_label = Label(f3, text="Width", font=("Arial", 10))
width_label.grid(row=1, column=0)

w = IntVar()

w = Entry(f3, textvariable= w)
w.grid(row=1, column=1, pady=5)

length_label = Label(f3, text="Length", font=("Arial", 10))
length_label.grid(row=2, column=0)

l = IntVar()

l = Entry(f3, textvariable= l)
l.grid(row=2, column=1, pady=5)

rectangle_area = Label(f3, text="", font=("Arial", 10))
rectangle_area.grid(row=3, column=1, columnspan=2)

rectangle_button = Button(f3, text="Calculate", command=rect_area_display)
rectangle_button.grid(row=4, column=1, pady=5)

root.mainloop()
