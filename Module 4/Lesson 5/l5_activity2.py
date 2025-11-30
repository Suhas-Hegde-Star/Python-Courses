s1, s2 = {1, 2, 3}, {"a", "b", "c"}
print(list(zip(s1, s2)))

l1, l2 = [x for x in range(0, 101, 10)], [x*10 for x in range(0, 101, 10)]
print(list(zip(l1, l2[::-1])))

stocks = ["APPLE", "GOOGLE", "MICROSOFT", "AMAZON", "TESLA", "META", "NETFLIX", "IBM", "INTEL", "AMD", "SAMSUNG"]
prices = [145.09, 2738.27, 299.35, 3344.94, 709.74, 358.32, 593.33, 142.15, 54.12, 103.25, 1375.50]
print({stocks:prices for stocks, prices in zip(stocks, prices)})