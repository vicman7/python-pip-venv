import random

OPTIONS = ("rock", "paper", "scissors")  # Moved to the top and renamed


def computer_choice():
    """Gets a random option for the computer to use."""
    computer = random.choice(OPTIONS)
    return computer


def user_choice():
    """Gets the option the player will use."""
    while True:
        user = input("Select what you want to play this round: Rock, Paper, Scissors.\n").strip().lower()
        if user in OPTIONS:
            return user
        print("Your choice is not valid. Check for typos and try again.")


def run_game():
    """Starts and handles the game from start to finish."""

    rounds = 3
    user_win = 0
    computer_win = 0

    print("*" * 15)
    print("The game will start now.")
    print("*" * 15)

    while True:

        computer = computer_choice()
        user = user_choice()
        print(f"{user} vs {computer}, ")

        if user == computer:

            rounds -= 1
            print(f"""

            Tie!
            You have both picked {user}
            {rounds} remaining.

            """)

        if (user == "scissors" and computer == "paper") or (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock"):

            rounds -= 1
            user_win += 1

            print(f"""

            You have won this round!
            {user} beats {computer}!
            {rounds} remaining.

            """)

        if (computer == "scissors" and user == "paper") or (computer == "rock" and user == "scissors") or (computer == "paper" and user == "rock"):

            rounds -= 1
            computer_win += 1

            print(f"""

            You have lost this round.
            {computer} beats {user}!
            {rounds} remaining.

            """)

        if rounds <= 0:
            winner_message = winner(user_win, computer_win)
            print(winner_message)
            print(f"You won {user_win} rounds, and the computer won {computer_win} rounds.")
            break
        

def winner(user_win, computer_win):
    """Determines the winner of the game."""
    if user_win > computer_win:
        return "You win!"
    elif computer_win > user_win:
        return "Computer wins!"
    else:
        return "It's a tie!"

def main():
    while True:
        run_game()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()