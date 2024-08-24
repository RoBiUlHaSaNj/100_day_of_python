#guessing_game_number


import random

def number_guessing_game():
    # Step 1: Set up the game
    secret_number = random.randint(1, 10)
    guess = None
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?")

    # Step 2: Loop until the user guesses the correct number
    while guess != secret_number:
        # Step 3: User Input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 4: Provide Feedback
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number: {secret_number}")  #f string 
            print(f"It took you {attempts} attempts.")

    # Step 5: Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("Thank you for playing! Goodbye.")

# Start the game
number_guessing_game()
