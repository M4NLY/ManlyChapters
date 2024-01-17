from tkinter import *

def getvals():
    print(f"The username you have registered is {userval.get()}")
    print(f"The password you have registered is {passval.get()}")
    
root = Tk()

user = Label(root, text="Username:")
password = Label(root, text="Password:")
user.grid(row=0, column=0)
password.grid(row=1, column=0)

userval = StringVar()
passval = StringVar()

userentry = Entry(root, textvariable=userval)
passentry = Entry(root, textvariable=passval, show='*')
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

submit = Button(root, text="Submit", command=getvals)    
submit.grid(row=2, column=1)

root.mainloop()

