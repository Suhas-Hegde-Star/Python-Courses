# Define the function to check the answer
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
print("ANIMAL QUIZ !!")

guess1 = input("\nWho is the God of Cricket?(Full Name) ")
check_guess(guess1, "Sachin Ramesh Tendulkar")

# Print the total score
print("\nYour score is", str(score))