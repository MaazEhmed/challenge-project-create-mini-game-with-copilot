import random

def get_player_choice():
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ["rock", "paper", "scissors"]:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    if (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    return "Computer wins!"

def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"Player chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Player's score: {player_score}")
    print(f"Computer's score: {computer_score}")


if __name__ == "__main__":
    main()
