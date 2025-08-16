name = input("Enter your name ")
age = input("Enter your age ")
height = input("Enter your height ")
weight = input("Enter your weight ")
vacccinate = input("Are you vaccinated? ")

if vacccinate.lower() == "yes":
    vacccinate = True
else:
    vacccinate = False

print ("Type of name is", type(name))
print ("Type of age is", type(age))
print ("Type of height is", type(height))
print ("Type of weight is", type(weight))
print ("Type of vaccination is", type(vacccinate))