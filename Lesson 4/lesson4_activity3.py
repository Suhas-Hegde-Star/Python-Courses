eng = float(input("Enter your marks for english "))
bio = float(input("Enter your marks for biology "))
che = float(input("Enter your marks for chemistry "))
phy = float(input("Enter your marks for physics "))
mat = float(input("Enter your marks for maths "))
la2 = float(input("Enter your marks for language 2 "))
la3 = float(input("Enter your marks for language 3 "))

sum = eng + bio + che + phy + mat + la2 + la3
avg = (sum) / 7
percent = (sum / 700) * 100

if eng or bio or che or phy or mat or la2 or la3 > 100:
    print("invalid input")
elif eng or bio or che or phy or mat or la2 or la3 < 0:
    print("invalid input")
else:
    print("Your average marks is", avg)
    print("Your totsl marks is", sum)
    print("Your percentage is", percent)