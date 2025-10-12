x = []

for i in range(100):
    x.append(i + 1)

for i in range(101):
    if i % 5 == 0:
        continue
    print(i)
