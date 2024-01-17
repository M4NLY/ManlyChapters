from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


def update_order():
    coffee = coffee_var.get()
    sugar = sugar_var.get()
    milk = milk_var.get()
    messagebox.showinfo('Order', f"Your order is a {coffee} with {sugar} sugar and {milk} milk.")


#Main Frame


root = Tk()
root.title("Coffee Vending Machine")
root.resizable(False, False)


#Frame


frame = Frame(root)
frame.pack(padx=10)


#Title


title = Label(frame, text="Latte to Go", fg="black", font=("Helvetica", 15, "bold"))
title.pack(padx=10)


#coffee


coffee_var = StringVar()


coffee_label = Label(frame, text = "     DRINKS     ", fg="black", font=("Helvetica", 12, "bold"), padx= 10, pady=10).pack(padx=10, pady=10)


#Espresso
img1 = Image.open("image.png")
espresso = ImageTk.PhotoImage(img1.resize((100,100)))


espresso_label = Label(frame, image=espresso)
espresso_label.pack(side="left", padx=24)


espresso_text = Radiobutton(frame, text="Espresso", fg="black", font=("Helvetica", 10, "bold" ), variable=coffee_var, value="espresso")
espresso_text.pack(side="left")


#Latte


img2 = Image.open("image (4).png")
latte = ImageTk.PhotoImage(img2.resize((100,100)))


latte_label = Label(frame, image=latte)
latte_label.pack(side = "left", padx=10)


latte_text = Radiobutton(frame, text="Latte", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="latte", padx=10)
latte_text.pack(side="left")


#Cappuccino


frame2 = Frame(root)
frame2.pack(padx=10)


img3 = Image.open("image (1).png")
cap = ImageTk.PhotoImage(img3.resize((100,100)))


cap_label = Label(frame2, image=cap)
cap_label.pack(side="left", padx=10)


cap_text = Radiobutton(frame2, text="Cappuccino", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="cappuccino")
cap_text.pack(side="left")


#Mocha


img4 = Image.open("image (3).png")
mocha = ImageTk.PhotoImage(img4.resize((100,100)))


mocha_label = Label(frame2, image=mocha)
mocha_label.pack(side="left")


mocha_text = Radiobutton(frame2, text="Mocha", fg="black", font=("Helvetica", 10, "bold"), variable=coffee_var, value="mocha")
mocha_text.pack(side="left", padx=20)


#Sugar


frame3 = Frame(root)
frame3.pack()


sugar_var = StringVar()


sugar_label = Label(frame3, text = "      SUGAR      ",fg="black", font=("Helvetica", 12, "bold"), padx= 10, pady=10)
sugar_label.pack(padx=142, pady=20)


zero = Radiobutton(frame3, text="0%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="no")
zero.pack(side="left", padx=20)


twenty_five = Radiobutton(frame3, text="25%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="25%")
twenty_five.pack(side="left", padx=20)


fifty = Radiobutton(frame3, text="50%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="50%")
fifty.pack(side="left", padx=20)


seventy_five = Radiobutton(frame3, text="75%", fg="black", font=("Helvetica", 13, "bold"), variable=sugar_var, value="75%")
seventy_five.pack(side="left", padx=20)


#Milk


frame4 = Frame(root)
frame4.pack()


milk_var = StringVar()


milk_label =Label(frame4, text = "         MILK         ", fg="black", font=("Helvetica", 12, "bold"), padx= 10, pady=10)
milk_label.pack(padx=20, pady=20)


skimmed = Radiobutton(frame4, text="Soy", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="soy")
skimmed.pack(side="left", padx=20)


almond = Radiobutton(frame4, text="Coconut", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="coconut")
almond.pack(side="left", padx=12)


oat = Radiobutton(frame4, text="Condensed", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="condensed")
oat.pack(side="left", padx=12)


low_fat = Radiobutton(frame4, text="Whole", fg="black", font=("Helvetica", 10, "bold"), variable=milk_var, value="whole")
low_fat.pack(side="left", padx=20)


#Order


frame5 = Frame(root)
frame5.pack()


order_button = Button(frame5, text="ORDER", bg="grey",fg="black", font=("Helvetica", 12, "bold"), padx= 10, pady=5, bd=0, command= update_order)
order_button.pack(padx=169, pady=10)


order_text = Label(frame5, text="", font=("Helvetica", 10))
order_text.pack(pady=10)




root.mainloop()
