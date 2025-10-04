import random

def weather(cond):
    if cond == 1:
        print("It is rainy outside.")
    elif cond == 2:
        print("It is sunny outside.")
    elif cond == 3:
        print("It is cloudy outside.")
    elif cond == 4:
        print("It is snowy outside.")
    else:
        print("I do not know what the weather is like")

weath = random.randint(1, 6)
weather(weath)