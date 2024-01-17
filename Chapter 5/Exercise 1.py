from tkinter import *
from tkinter import messagebox

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def woof(self):
        return f"{self.name} says Woof!"

    @classmethod
    def oldest_dog_woof(cls, dog1, dog2):
        oldest_dog = dog1 if dog1.age > dog2.age else dog2
        messagebox.showinfo("Oldest Dog Woof", oldest_dog.woof())

class DogGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Dog Information")

        # Dog 1
        self.dog1_label = Label(master, text="Dog 1:")
        self.dog1_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.dog1_name_label = Label(master, text="Name:")
        self.dog1_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.dog1_name_entry = Entry(master)
        self.dog1_name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.dog1_age_label = Label(master, text="Age:")
        self.dog1_age_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.dog1_age_entry = Entry(master)
        self.dog1_age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.dog1_breed_label = Label(master, text="Breed:")
        self.dog1_breed_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.dog1_breed_entry = Entry(master)
        self.dog1_breed_entry.grid(row=3, column=1, padx=10, pady=5)

        # Dog 2
        self.dog2_label = Label(master, text="Dog 2:")
        self.dog2_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        self.dog2_name_label = Label(master, text="Name:")
        self.dog2_name_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        self.dog2_name_entry = Entry(master)
        self.dog2_name_entry.grid(row=5, column=1, padx=10, pady=5)

        self.dog2_age_label = Label(master, text="Age:")
        self.dog2_age_label.grid(row=6, column=0, padx=10, pady=5, sticky=W)
        self.dog2_age_entry = Entry(master)
        self.dog2_age_entry.grid(row=6, column=1, padx=10, pady=5)

        self.dog2_breed_label = Label(master, text="Breed:")
        self.dog2_breed_label.grid(row=7, column=0, padx=10, pady=5, sticky=W)
        self.dog2_breed_entry = Entry(master)
        self.dog2_breed_entry.grid(row=7, column=1, padx=10, pady=5)

        # Button
        self.submit_button = Button(master, text="Submit", command=self.display_dog_info)
        self.submit_button.grid(row=8, column=0, columnspan=2, pady=10)

    def display_dog_info(self):
        # Get data from the entries
        dog1_name = self.dog1_name_entry.get()
        dog1_age = int(self.dog1_age_entry.get())
        dog1_breed = self.dog1_breed_entry.get()

        dog2_name = self.dog2_name_entry.get()
        dog2_age = int(self.dog2_age_entry.get())
        dog2_breed = self.dog2_breed_entry.get()

        # Create Dog objects
        dog1 = Dog(dog1_name, dog1_age, dog1_breed)
        dog2 = Dog(dog2_name, dog2_age, dog2_breed)

        # Display dog information
        messagebox.showinfo("Dog 1 Info", f"{dog1.name} - Age: {dog1.age}, Breed: {dog1.breed}")
        messagebox.showinfo("Dog 2 Info", f"{dog2.name} - Age: {dog2.age}, Breed: {dog2.breed}")

        # Make the oldest dog woof
        Dog.oldest_dog_woof(dog1, dog2)

if __name__ == "__main__":
    root = Tk()
    dog_gui = DogGUI(root)
    root.mainloop()
