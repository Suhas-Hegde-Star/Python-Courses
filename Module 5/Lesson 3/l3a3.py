class bird:
    def __init__(self):
        print("Bird is created")  

    def fly(self):
        return "Bird is flying."

    def sing(self):
        return "Bird is singing."
    
class pengpeng(bird):
    def __init__(self):
        super().__init__()
        print("Pengpeng is created")

    def fly(self):
        return "Pengpeng is flying."
    
    def swim(self):
        return "Pengpeng is swimming."
    
p = pengpeng()
print(p.sing())
print(p.fly())
print(p.swim())