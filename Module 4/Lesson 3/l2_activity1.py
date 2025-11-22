squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(squares)

item = squares.items()
for i in item:
    print(i)

print(squares.get(4))
print(squares.keys())
print(squares.values())