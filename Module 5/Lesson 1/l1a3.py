class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

print("{blu.name} is {blu.age} years old".format(blu=blu, woo=woo))
print("{woo.name} is {woo.age} years old".format(blu=blu, woo=woo))