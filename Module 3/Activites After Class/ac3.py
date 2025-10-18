def bill(tb, given, due):
    """Calculate the bill amount that is yet to be paid"""
    if given > due:
        return f"You have paid {given - due} extra"
    elif due > given:
        return f"You still owe {due - given}"
    else:
        return "You have paid the exact amount"
    
total_bill = int(input("Enter the total bill amount: "))
amount_given = int(input("Enter the amount given: "))

bill((total_bill), (amount_given), (total_bill - amount_given))