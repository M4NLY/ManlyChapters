from tkinter import *

def draw_shape():
    shape = shape_var.get()
    coord = coord_entry.get()

    if shape == "Oval":
        canvas.create_oval(coord, fill="lightblue")
    elif shape == "Rectangle":
        canvas.create_rectangle(coord, fill="lightblue")
    elif shape == "Square":
        x1, y1, x2, y2 = map(int, coord.split())
        side_length = min(x2 - x1, y2 - y1)
        canvas.create_rectangle(x1, y1, x1 + side_length, y1 + side_length, fill="lightblue")
    elif shape == "Triangle":
        points = list(map(int, coord.split()))
        canvas.create_polygon(points, fill="lightblue")

root = Tk()
root.title("Shape Drawer")

canvas = Canvas(root, width=400, height=400)
canvas.pack()

shape_var = StringVar()
shape_var.set("Oval")

shape_lbl = Label(root, text="Pick a shape")
shape_lbl.pack()

shape_menu = OptionMenu(root, shape_var, "Oval", "Rectangle", "Square", "Triangle")
shape_menu.pack()

coord_lbl = Label(root, text="Enter your coordinates (x1 y1 x2 y2 or x1 y1 x2 y2 x3 y3) [DO NOT PUT COMMAS]: ")
coord_lbl.pack()

coord_entry = Entry(root)
coord_entry.pack()

draw_btn = Button(root, text="Draw", command=draw_shape)
draw_btn.pack()

root.mainloop()
