import random

play = True
num = str(random.randint(1, 100))
log = []

print("Welcome to the Number Guessing Game!")
tries = 0

while play:
    guess = input("Enter your guess (or type 'e' to quit): ")

    if guess == 'e':
        play = False
        tries += 1
        print("Thanks for playing!")
        log.append("Game ended by user.\n")
        log.append(f"Total tries: {tries}\n")
        break
    elif guess == "g":
        print(f"The number is: {num}")
        log.append(f"User requested the number: {num}\n")
        play = False
        break
    elif guess == num:
        tries += 1
        print(f"Congratulations! You've guessed the number {num} in {tries} tries.")
        log.append(f"Guessed the number {num} in {tries} tries.\n")
        play = False
        break
    elif (guess < num) and (int(num) - int(guess) <= 10):
        tries += 1
        print("Low! Try again.")
        log.append(f"Guess: {guess} - Low\n")
    elif (guess > num) and (int(guess) - int(num) <= 10):
        tries += 1
        print("High! Try again.")
        log.append(f"Guess: {guess} - High\n")
    elif guess < num:
        tries += 1
        print("Too Low! Try again.")
        log.append(f"Guess: {guess} - Low\n")
    elif guess > num:
        tries += 1
        print("Too High! Try again.")
        log.append(f"Guess: {guess} - High\n")
    else:
        print("Invalid input. Please enter a number between 1 and 100 or 'e' to quit.")
        log.append(f"Invalid input: {guess}\n")

with open("guessing_game_log.txt", "a") as f:
    f.writelines(log)
f.close()