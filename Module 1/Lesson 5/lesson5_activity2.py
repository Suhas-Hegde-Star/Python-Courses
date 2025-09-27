CP = float(input("Enter Cost Price: "))
SP = float(input("Enter Selling Price: "))

if SP > CP:
    print("Profit")
    print("Profit is", SP - CP)
elif CP > SP:
    print("Loss")
    print("Loss is", CP - SP)
else : 
    print("No Profit nor Loss")