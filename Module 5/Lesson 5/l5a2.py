from abc import ABC as a
from abc import abstractmethod as b

class Car(a):
    def __init__(self, fuels, color):
        super().__init__()
        self.fuels = fuels
        self.color = color

    @b
    def mileage(self):
        pass

    @b
    def max_speed(self):
        pass

    @b
    def aura(self):
        pass

class Lambhorgini(Car):
    def __init__(self, fuels, color):
        super().__init__(fuels, color)
        self.name = "Lambhorgini"

    def printer(self):
        print(self.name, "with fuel type:", self.fuels, "and color:", self.color)

    def mileage(self):
        print("Mileage is 100 km/l")

    def max_speed(self):
        print("Max Speed is 400 km/h")

    def aura(self):
        print("Aura is Godly and Stunning")

obj = Lambhorgini("Truck", "Red")

obj.printer()
obj.mileage()
obj.max_speed()
obj.aura()

