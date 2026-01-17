import random
import time

# Dictionary of 50 color of food
fruit_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grapes": "Purple",
    "Orange": "Orange",
    "Lemon": "Yellow",
    "Blueberry": "Blue",
    "Kiwi": "Brown",
    "Mango": "Yellow",
    "Strawberry": "Red",
    "Watermelon": "Green",
    "Pineapple": "Yellow",
    "Cherry": "Red",
    "Peach": "Pink",
    "Plum": "Purple",
    "Raspberry": "Red",
    "Blackberry": "Black",
    "Cantaloupe": "Orange",
    "Papaya": "Orange",
    "Coconut": "Brown",
    "Fig": "Purple",
    "Pomegranate": "Red",
    "Tangerine": "Orange",
    "Cranberry": "Red",
    "Apricot": "Orange",
    "Grapefruit": "Pink",
    "Passion Fruit": "Purple",
    "Dragon Fruit": "Pink",
    "Jackfruit": "Yellow",
    "Starfruit": "Yellow",
    "Durian": "Green",
    "Persimmon": "Orange",
    "Currant": "Red",
    "Gooseberry": "Green",
    "Quince": "Yellow",
    "Ugli Fruit": "Green",
    "Breadfruit": "Green",
    "Salak": "Brown",
    "Longan": "Brown",
    "Lychee": "Red",
    "Rambutan": "Red",
    "Soursop": "Green",
    "Jujube": "Red",    
    "Medlar": "Brown",
    "Cloudberry": "Orange",
    "Huckleberry": "Blue",
    "Boysenberry": "Purple",    
    "Elderberry": "Black",
    "Marionberry": "Purple",
    "Salmonberry": "Orange",
    "Tamarind": "Brown"
}


class Chooooooooooo():
    def __init__(self, color):
        self.color = color

    def get_question(self):
        fruit, color = random.choice(list(fruit_colors.items()))
        question = f"What is the color of {fruit}?"
        return question, color
        
    def check_guess(guess, answer):
        global score
        still_guessing = True
        attempt = 0
        while still_guessing and attempt < 3:
            if guess.lower() == answer.lower():
                print("Correct Answer")
                score = score + 1
                still_guessing = False
            else:
                if attempt < 2:
                    guess = input("Sorry, Wrong answer. Try again")
                attempt = attempt + 1

        if attempt == 3:
            print("The correct answer is", answer)

score = 0
print("Fruit QUIZZZZZ !!")

while True:
    ch = Chooooooooooo("any")
    question, answer = ch.get_question()
    print(question)
    start_time = time.time()
    guess = input(f"You have to answer: ")

    if guess == answer:
        print("Correct Answer")
        score = score + 1
    else:
        Chooooooooooo.check_guess(guess, answer)
        print("The correct answer is", answer)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break