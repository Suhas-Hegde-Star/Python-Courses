num = int(input("Enter the tables to be found: "))
print("The tables of {} is :".format(num))

for i in range (1, 11):
    print("{} * {} = {}".format(num, i, num * i))