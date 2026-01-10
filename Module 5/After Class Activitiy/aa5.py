class Vehicle:
    def __init__(self, selfy):
        self.selfy = selfy

    def feul_type(self):
        pass

    def max_speed(self):
        pass

class BMW(Vehicle):
    def __init__(self):
        super().__init__("BMW")

    def feul_type(self):
        print(self.selfy, "uses Diesel as feul type")

    def max_speed(self):
        print(self.selfy, "has max speed of 250 km/h")

class Bugati_is_Suhas(Vehicle):
    def __init__(self):
        super().__init__("Bugati_is_Suhas")

    def feul_type(self):
        print(self.selfy, "uses Petrol as feul type")

    def max_speed(self):
        print(self.selfy, "has max speed of 450 km/h")

obj = BMW()
obj.feul_type()
obj.max_speed()

obj2 = Bugati_is_Suhas()
obj2.feul_type()
obj2.max_speed()