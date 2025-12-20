class vehicle:
    
    def __init__(self, mil, mox):
        self.mil = str(mil) + " kmph"
        self.max = str(mox) + " kmph"
    
mod1 = vehicle(10, 50)

print("Mileage is:   ", mod1.mil)
print("Max speed is: ", mod1.max)