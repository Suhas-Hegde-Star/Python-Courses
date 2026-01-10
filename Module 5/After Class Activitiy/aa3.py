class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.total_charge = 0

    def calculate_charge(self):
        self.total_charge = self.capacity * (self.capacity/10)
        return self.total_charge
    
class Bus(Vehicle):
    def calculate_charge(self):
        self.total_charge = self.capacity * (self.capacity/10) + 3500
        return self.total_charge

obj=Bus(50)
print("Total Charge for Bus with capacity", obj.capacity, "is:", obj.calculate_charge())
