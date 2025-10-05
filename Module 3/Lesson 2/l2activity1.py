def bill(para1, para2):
    print(f"Total bill is {para1}")
    tipf = (para2 * para1) / 100
    print(f"Tip is {tipf}")
    print(f"Total amount is {para1 + tipf}")

bills = input("Enter the Amount in the Bill: ")
tip = input("Enter the Tip Percentage: ")

bill(int(bills), int(tip))