import random

# Step 1 & 2: Set up choices and mapping
choices = ["rock", "paper", "scissors"]
choice_map = {0: "rock", 1: "paper", 2: "scissors"}

def get_player_choice():
    """Step 1: Get and validate player input"""
    while True:
        player_input = input("Enter rock, paper, or scissors: ").lower().strip()
        
        # Step 3: Validate input
        if player_input in choices:
            return player_input
        else:
            print("Invalid choice! Please enter rock, paper, or scissors.\n")

def get_computer_choice():
    """Step 2: Generate random computer choice"""
    random_index = random.randint(0, 2)
    return choice_map[random_index]

def determine_winner(player, computer):
    """Step 4 & 5: Apply game rules to determine outcome"""
    
    # Tie condition
    if player == computer:
        return "tie"
    
    # Player win conditions
    winning_moves = {
        "rock": "scissors",      # rock beats scissors
        "scissors": "paper",     # scissors beats paper
        "paper": "rock"          # paper beats rock
    }
    
    if winning_moves[player] == computer:
        return "win"
    else:
        return "loss"

def display_result(player, computer, result):
    """Step 6: Display outcome"""
    print(f"\nYou played: {player}")
    print(f"Computer played: {computer}")
    
    if result == "tie":
        print("Result: It's a tie! 🤝")
    elif result == "win":
        print("Result: You win! 🎉")
    else:
        print("Result: Computer wins! 🤖")
    print()

def play_again():
    """Step 7: Ask if player wants to continue"""
    response = input("Play again? (yes/no): ").lower().strip()
    return response in ["yes", "y"]

def main():
    """Main game loop"""
    print("=== Rock Paper Scissors ===\n")
    
    score = {"wins": 0, "losses": 0, "ties": 0}
    
    while True:
        # Step 1: Get player input
        player_choice = get_player_choice()
        
        # Step 2: Generate computer choice
        computer_choice = get_computer_choice()
        
        # Step 4 & 5: Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        # Step 6: Display result
        display_result(player_choice, computer_choice, result)
        
        # Update score
        score[{"win": "wins", "loss": "losses", "tie": "ties"}[result]] += 1
        print(f"Score - Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")
        
        # Step 7: Loop logic - ask to play again
        if not play_again():
            print("\nFinal score:")
            print(f"Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()