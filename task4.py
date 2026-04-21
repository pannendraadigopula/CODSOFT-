import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if wins[player] == computer:
        return "player"
    return "computer"

def display_result(player, computer, result, scores):
    emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    print(f"\n  You chose   : {emoji[player]}  {player.capitalize()}")
    print(f"  Computer chose: {emoji[computer]}  {computer.capitalize()}")
    print("-" * 30)
    if result == "tie":
        print("  It's a TIE! 🤝")
    elif result == "player":
        print("  You WIN! 🎉")
    else:
        print("  Computer WINS! 🤖")
    print(f"\n  Score -> You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['tie']}")

def main():
    print("\n==============================")
    print("   ROCK - PAPER - SCISSORS   ")
    print("==============================")

    scores = {"player": 0, "computer": 0, "tie": 0}

    while True:
        print("\nChoose your move:")
        print("  1. Rock")
        print("  2. Paper")
        print("  3. Scissors")
        print("  4. Quit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == "4":
            print("\n--- Final Scores ---")
            print(f"You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['tie']}")
            print("Thanks for playing! Goodbye!")
            break

        moves = {"1": "rock", "2": "paper", "3": "scissors"}

        if choice not in moves:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            continue

        player_choice   = moves[choice]
        computer_choice = get_computer_choice()
        result          = get_winner(player_choice, computer_choice)

        scores[result] += 1

        print("-" * 30)
        display_result(player_choice, computer_choice, result, scores)

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n--- Final Scores ---")
            print(f"You: {scores['player']}  |  Computer: {scores['computer']}  |  Ties: {scores['tie']}")
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
