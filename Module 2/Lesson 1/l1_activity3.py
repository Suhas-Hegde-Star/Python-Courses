dest = int(input("Enter the distance to be traveled (in km): "))
vehicle_type = input("Enter the vehicle type\n1. Car\n2. Bike\n3. Bus\n4. Luxury Car\n")
vehicle = None

if vehicle_type.lower() == "car" or vehicle_type == "1":
    milage = 35
    comfort = 75
elif vehicle_type.lower() == "bike" or vehicle_type == "2":
    milage = 40
    comfort = 50
elif vehicle_type.lower() == "bus" or vehicle_type == "3":
    milage = 25
    comfort = 60
elif vehicle_type.lower() == "luxury car" or vehicle_type == "4":
    milage = 20
    comfort = 95

price = dest / milage
f_price = (price * comfort) * 15

print("The fare for the journey is: ₹", round(f_price, 0))