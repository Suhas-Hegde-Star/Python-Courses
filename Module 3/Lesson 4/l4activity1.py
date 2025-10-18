import datetime

one = str(datetime.datetime.now())
log = []
number_of_inputs = int(input("How many numbers do you want to enter? "))

for i in range(number_of_inputs):
    try:
        x = int(input("Enter a number: "))
        print("You entered:", x)
        log.append(one + " : Valid Input")
        log.append("\n")

    except ValueError as ex:
        print("Error details:", ex)
        log.append(one + " : Invalid Input")
        log.append("\n")

with open("log.txt", "a") as f:
    f.writelines(log)
