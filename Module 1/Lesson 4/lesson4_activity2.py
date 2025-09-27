amount = int(input("Enter amount: "))

n500 = amount // 500
n200 = (amount % 500) // 200
n100 = ((amount % 500) % 200) // 100
n50 = (amount % 100) // 50
n20 = (amount % 20) // 20
n10 = (amount % 50) // 10
n5 = (amount % 10) // 5
n2 = (amount % 2) // 2
n1 = (amount % 5) // 1

print ("500 note:", n500)
print ("200 note:", n200)
print ("100 note:", n100)
print ("50 note:", n50)
print ("20 note:", n20)
print ("10 coin:", n10)
print ("5 coin:", n5)
print ("2 coin:", n2)
print ("1 coin:", n1)

print("Total notes:", n500 + n200 + n100 + n50 + n20)
print("Total coins:", n10 + n5 + n2 + n1)
print("Total notes and coins:", n500 + n200 + n100 + n50 + n20 + n10 + n5 + n2 + n1)
print("Thank you for using this service")