class fruit:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def intro(self):
        print("I am a fruit of " + self.color + " and my name is " + self.name)

orange = fruit("Orange", "Orange")
orange.intro()

del orange

try:
    orange.intro()
except NameError as e:
    print("Error:", e)