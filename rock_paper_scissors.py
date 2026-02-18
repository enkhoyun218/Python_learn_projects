import random


options = ["rock", "paper", "scissors"]

scores = {"player": 0, "computer": 0, "ties": 0}

print("Welcome to the Python Battle!")


while scores["player"] < 3 and scores["computer"] < 3:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in options:
        print("Invalid choice, try again.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        scores["ties"] += 1
        print(f"Score — You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    elif user_choice == "rock" and computer_choice == "scissors":
        scores["player"] += 1
        print(f"Score — You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    elif user_choice == "scissors" and computer_choice == "paper":
        scores["player"] += 1
        print(f"Score — You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    elif user_choice == "paper" and computer_choice == "rock":
        scores["player"] += 1
        print(f"Score — You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['ties']}")
    else:
        scores["computer"] += 1
        print(f"Score — You: {scores['player']} | Computer: {scores['computer']} | Ties: {scores['ties']}")

if scores["player"] == 3:
    print("You won the match!")
else:
    print("Computer wins the match!")

