class Animal:
    def speak(self):
        print("Ha Ha Ho He Ha HAHA")

class Dog(Animal):
    def speak(self):
        print("Woof Woof Woof Woof Woof")

class Cat(Animal):
    def speak(self):
        print("Meow Meow Meow Meow Meow")

class Cow(Animal):
    def speak(self):
        print("Moo Moo Moo Moo Moo")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
cat.speak()
cow.speak()

animal = Animal()
animal.speak()