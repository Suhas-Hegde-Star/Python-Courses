unit = int(input("Enter the units of electricity consumed: "))

if unit <= 50:
    amount = unit * 2.60
    surcharge = 25
elif unit <= 100:
    amount = 130 + ((unit - 50) * 3.25)
    surcharge = 35
elif unit <= 200:
    amount = 130 + 162.5 + ((unit - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.5 + 526 + ((unit - 200) * 7.87)
    surcharge = 55

percent_surcharge = (surcharge / 100) * amount
percent = round(percent_surcharge, 2)
total_amount = amount + surcharge

print("Total amount to be paid:", total_amount)
print("Surcharge amount:", str(percent)+"%")