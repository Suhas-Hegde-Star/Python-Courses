class bird:
    def __init__(self):
        print("Bird is created")  

    def fly(self):
        return "Bird is flying."

    def sing(self):
        return "Bird is singing."
    
class pengpengpengwin(bird):
    def __init__(self):
        super().__init__()
        print("Pengpengpengwin is created")

    def fly(self):
        return "Pengpengpengwin is flying."
    
    def swim(self):
        return "Pengpengpengwin is swimming."
    
p = pengpengpengwin()
print(p.sing())
print(p.fly())
print(p.swim())