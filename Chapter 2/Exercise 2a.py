from tkinter import *

root = Tk()

root.geometry("200x75")


top = Frame(root)
top.pack(side = "top", fill="x")

a = Label(top, text="A", justify="center", bg="red", bd="5", relief="sunken")
a.pack(fill="x")

mid = Frame(root)
mid.pack(side="top", fill="x")

c = Label(mid, text="C", justify="center", bg="blue")
c.pack(side = "left", fill="x", expand= True)

d = Label(mid, text="D", justify="center", bg="white")
d.pack(side = "right", fill="x", expand= True)

b = Label(root, text="B", justify="center", bg="yellow", bd="2", relief="raised")
b.pack(side = "top", fill="x", padx="50")

root.mainloop()