
# Rock, Paper, Scissors Game


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get user input
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue

        # Get computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break


# Start the game
play_game()
