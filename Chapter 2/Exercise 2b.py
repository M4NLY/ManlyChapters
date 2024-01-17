from tkinter import *

root = Tk()
root.title("GUI Pack Example")

#frame
left_frame = Frame(root, bg="gray", bd=3)
right_frame = Frame(root, bg="gray", bd=3)

#pack the frames

left_frame.pack(side="left", expand= True, padx= "2")
right_frame.pack(side="right", expand= True, padx= "2")

#labels

label_a = Label(left_frame, text= "A", bg = "#22263D", fg="white", padx = "77", pady= "47")
label_b = Label(left_frame, text= "B", bg = "white", fg="black", padx="77", pady= "47")
label_c = Label(right_frame, text= "C", bg = "white", fg="black", padx="77", pady= "47")
label_d = Label(right_frame, text= "D", bg = "#22263D", fg="white", padx="77", pady="47")

#packing the labels

label_a.pack(in_= left_frame, expand= True, side="top")
label_b.pack(in_= left_frame, expand= True, side="bottom")
label_c.pack(in_= right_frame, expand= True, side="top")
label_d.pack(in_= right_frame, expand= True, side="bottom")

root.mainloop()
