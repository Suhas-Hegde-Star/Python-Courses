temp = input("Enter a temperature: ")

if temp > 0 and temp < 20:
    print("It's freezing!")
    print("Wear a heavy coat.")
elif temp > 20 and temp < 30:
    print("It's cold.")
    print("Wear a jacket.")
elif temp > 30 and temp < 40:
    print("It's warm.")
    print("Wear a light sweater.")
elif temp >= 40: 
    print("It's hot.")
    print("Stay hydrated!")
