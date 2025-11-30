l1, l2, l3 = [x for x in range(1, 11) ], [x for x in range(11, 21) ], []
l3 = list(map(lambda x, y: x + y, l1, l2))
for i in l3: print(i)