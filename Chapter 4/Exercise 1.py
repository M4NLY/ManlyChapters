from tkinter import *

def save_data():
    
    userdata = userval.get() 
    agedata = ageval.get()
    homedata = homeval.get()
    
    with open("bio.txt", "w") as file:
        file.write(f"{userdata}\n{agedata}\n{homedata}")
    print(f"Username: {userdata}\nAge: {agedata}\nHometown: {homedata}\n")

root = Tk()
root.resizable(False, False)

user_label = Label(root, text="Username").grid(row = 0, column = 0)
userval = StringVar()
user_input = Entry(root, textvariable=userval).grid(row = 0, column = 1)

age_label = Label(root, text="Age").grid(row=1, column=0)
ageval = IntVar(value="")
age_input = Entry(root, textvariable=ageval).grid(row = 1, column = 1)

home_label = Label(root, text="Hometown").grid(row=2, column=0)
homeval = StringVar()
home_input = Entry(root, textvariable=homeval).grid(row=2, column=1)

save_btn = Button(root, text="Save Data", command=save_data).grid(row=3, column=1)

root.mainloop()