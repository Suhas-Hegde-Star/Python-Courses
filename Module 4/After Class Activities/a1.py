s, ss = int(input("Enter A start number: ")), int(input("Enter A stop number: "))
l = []

for i in range(s, ss + 1):
    l.append(i ** 2)

for i in l:
    if i % 2 == 0:
        print("Even square:", i)
    else:
        print("Odd square:", i)