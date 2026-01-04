class Student:

    __admin_code = "ADmIN6767"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dislay_info(self):
        return f"\n\n\n\nName : {self.name}.\nAge: {self.age}.\nAdmin Code: {Student.__admin_code}.\n\n\n\n"
    
stduntentes = Student("Virat Kholi", 34)
try:
    print(stduntentes.__admin_code())
except AttributeError as e:
    print(e)
    print(stduntentes.dislay_info())
