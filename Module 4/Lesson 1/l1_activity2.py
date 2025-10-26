fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "voavanga", "watermelon", "xigua", "yellow passion fruit", "zucchini", "pop"]

for fruit in fruits:
    if fruit[0] == fruit[-1]:
        print(f"{fruit} starts and ends with the same letter.")
    else:
        print(f"{fruit} does not start and end with the same letter.")