class Employee:

    """
    Docstring for IOstring
    
            |--------|---------------|--------------------------------------|
            | Steps  |   Function    |         Description                  |
            |--------|---------------|--------------------------------------|
            |Step 1  | get_info      |  Get employee information            |
            |Step 2  | display_info  |  Display the employee information    |
            |--------|---------------|--------------------------------------|

    """

    def __init__(self):
        self.name = ""
        self.id = ""
        self.salary = ""

    def get_info(self):
        self.name = input("Enter employee name: ")
        self.id = input("Enter employee ID: ")
        self.salary = float(input("Enter employee salary: "))

    def display_info(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: ${self.salary:.2f}"
    
    def del_employee(self):
        choice = input("Enter the id of the employee to delete: ")
        if choice == self.id:
            del self
            print("Employee record deleted.")
        else:
            print("No matching employee ID found.")

    def run_all():
        self = Employee()
        self.get_info()
        print(self.display_info())
        self.del_employee()

for i in range(5):
    Employee.run_all()

choic = input("Do you want to delete an employee record? (yes/no): ")
if choic.lower() == 'yes':
    emp = Employee()
    emp.del_employee()
else:
    print("No records were deleted.")
    exit()