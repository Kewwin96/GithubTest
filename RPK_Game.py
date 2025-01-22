import random

# Possible choices
choices = ["Rock", "Paper", "Scissors"]

# Initialize scores
user_score = 0
computer_score = 0
rounds = 0
max_rounds = 5

print("Let's play Rock, Paper, Scissors! Best of 5 rounds wins.")

while rounds < max_rounds:
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Get user's choice with enhanced input validation
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").strip().capitalize()
    if user_choice.startswith("R"):
        user_choice = "Rock"
    elif user_choice.startswith("P"):
        user_choice = "Paper"
    elif user_choice.startswith("S"):
        user_choice = "Scissors"
    
    # Validate the user's choice
    if user_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue  # Skip the rest of the loop if input is invalid

    # Display choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner for this round
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Increase the round count
    rounds += 1
    print(f"Score - You: {user_score} | Computer: {computer_score}")
    print("-" * 30)  # Divider for readability

# Declare the overall winner
print("\nGame Over!")
if user_score > computer_score:
    print("Congratulations, you are the overall winner!")
elif computer_score > user_score:
    print("The computer is the overall winner. Better luck next time!")
else:
    print("It's a tie! Well played!")

print(f"Final Score - You: {user_score} | Computer: {computer_score}")