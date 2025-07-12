import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice. Please try again.")

def play_game():
    user_choice = get_user_choice()
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
        return 0  # tie
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        return 1  # user win
    else:
        print("You lose!")
        return -1  # user lose

def main():
    print("Welcome to Rock, Paper, Scissors!")
    rounds = 0
    wins = 0
    losses = 0
    while True:
        result = play_game()
        rounds += 1
        if result == 1:
            wins += 1
        elif result == -1:
            losses += 1
        again = input("Would you like to play again? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print(f"Thanks for playing! You won {wins} out of {rounds} rounds.")
            print(f"You lost {losses} rounds.")
            break

if __name__ == "__main__":
    main()
