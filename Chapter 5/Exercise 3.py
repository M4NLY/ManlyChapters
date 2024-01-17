from tkinter import messagebox, Tk, Label, Entry, Button, Text, END

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    def setData(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"


class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Data Entry")

        self.employees = []
        self.current_employee_index = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_name = Label(self.master, text="Name:")
        self.label_position = Label(self.master, text="Position:")
        self.label_salary = Label(self.master, text="Salary:")
        self.label_id = Label(self.master, text="ID:")

        self.entry_name = Entry(self.master)
        self.entry_position = Entry(self.master)
        self.entry_salary = Entry(self.master)
        self.entry_id = Entry(self.master)

        self.button_add_employee = Button(self.master, text="Add Employee", command=self.add_employee)
        self.button_display_employees = Button(self.master, text="Display Employees", command=self.display_employees)

        self.text_output = Text(self.master, height=10, width=50)

        # Grid layout
        self.label_name.grid(row=0, column=0)
        self.label_position.grid(row=1, column=0)
        self.label_salary.grid(row=2, column=0)
        self.label_id.grid(row=3, column=0)

        self.entry_name.grid(row=0, column=1)
        self.entry_position.grid(row=1, column=1)
        self.entry_salary.grid(row=2, column=1)
        self.entry_id.grid(row=3, column=1)

        self.button_add_employee.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_display_employees.grid(row=5, column=0, columnspan=2)

        self.text_output.grid(row=6, column=0, columnspan=2)

    def add_employee(self):
        name = self.entry_name.get()
        position = self.entry_position.get()
        salary = float(self.entry_salary.get())
        emp_id = int(self.entry_id.get())

        employee = Employee()
        employee.setData(name, position, salary, emp_id)
        self.employees.append(employee)

        # Clear the entry fields
        self.entry_name.delete(0, END)
        self.entry_position.delete(0, END)
        self.entry_salary.delete(0, END)
        self.entry_id.delete(0, END)

        messagebox.showinfo("Success", "Employee added successfully!")

    def display_employees(self):
        output_text = "Name\tPosition\tSalary\tID\n"
        output_text += "--------------------------------\n"
        for employee in self.employees:
            output_text += employee.getData() + "\n"

        self.text_output.delete(1.0, END)  # Clear previous content
        self.text_output.insert(END, output_text)


if __name__ == "__main__":
    root = Tk()
    app = EmployeeGUI(root)
    root.mainloop()
