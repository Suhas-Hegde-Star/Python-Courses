class person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(f"Name of the person is {self.name}.\nID number of the person is {self.id_number}")

class employee(person):
    def __init__(self, name, id_number, salary, position):
        self.salary = salary
        self.position = position
        super().__init__(name, id_number)

empempemployeeeee = employee("Virat Kholi", "6767", 100000, "Cricketer")
empempemployeeeee.display()