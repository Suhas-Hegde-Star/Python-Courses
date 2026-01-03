class dad():
    def __init__(self, eyes, hair):
        self.eyes = eyes
        self.hair = hair

    def display(self):
        print(f"Eye color of the person is {self.eyes}.\nHair color of a person is {self.hair}")

class child(dad):
    def __init__(self, eyes, hair, name, age):
        self.name = name
        self.age = age
        super().__init__(eyes, hair)

kiddo = child("brown", "black", "Tommy", 5)
kiddo.display()