from tkinter import *

class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        self.type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        return f"{self.name} says hello!"

    def makeNoise(self):
        return f"{self.name} makes a {self.noise} noise!"

    def animalDetails(self):
        details = f"Type: {self.type}\nName: {self.name}\nColor: {self.color}\nAge: {self.age}\nWeight: {self.weight}\nNoise: {self.noise}"
        return details


def create_animal():
    animal_type = animal_type_var.get()
    name = name_entry.get()
    color = color_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    noise = noise_entry.get()

    animal = Animal(animal_type, name, color, age, weight, noise)
    result_text.set(f"{animal.animalDetails()}\n{animal.sayHello()}\n{animal.makeNoise()}")


# Create the main application window
app = Tk()
app.title("Animal Details")

# Create widgets
label_type = Label(app, text="Type:")
label_name = Label(app, text="Name:")
label_color = Label(app, text="Color:")
label_age = Label(app, text="Age:")
label_weight = Label(app, text="Weight:")
label_noise = Label(app, text="Noise:")

animal_type_var = StringVar()
animal_type_var.set("Dog")

animal_type_menu = OptionMenu(app, animal_type_var, "Dog", "Cow")
name_entry = Entry(app)
color_entry = Entry(app)
age_entry = Entry(app)
weight_entry = Entry(app)
noise_entry = Entry(app)

btn_create_animal = Button(app, text="Create Animal", command=create_animal)

result_text = StringVar()
result_label = Label(app, textvariable=result_text)

# Arrange widgets in a grid
label_type.grid(row=0, column=0, padx=10, pady=5, sticky="e")
label_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_color.grid(row=2, column=0, padx=10, pady=5, sticky="e")
label_age.grid(row=3, column=0, padx=10, pady=5, sticky="e")
label_weight.grid(row=4, column=0, padx=10, pady=5, sticky="e")
label_noise.grid(row=5, column=0, padx=10, pady=5, sticky="e")

animal_type_menu.grid(row=0, column=1, padx=10, pady=5)
name_entry.grid(row=1, column=1, padx=10, pady=5)
color_entry.grid(row=2, column=1, padx=10, pady=5)
age_entry.grid(row=3, column=1, padx=10, pady=5)
weight_entry.grid(row=4, column=1, padx=10, pady=5)
noise_entry.grid(row=5, column=1, padx=10, pady=5)

btn_create_animal.grid(row=6, column=0, columnspan=2, pady=10)

result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Start the Tkinter main loop
app.mainloop()
