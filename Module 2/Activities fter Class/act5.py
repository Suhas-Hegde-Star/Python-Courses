def mirrored(r):
    for i in range(1, r + 1):
        print(" " * (r - i) + "#" * i)

mirrored(int(input("Enter the number of rows: ")))