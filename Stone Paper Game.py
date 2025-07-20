import random

options = ["stone", "paper", "scissors"]
attempts = 3
score = 0

print("Welcome to Stone Paper Scissors!")
print("You have 3 rounds. Type: stone / paper / scissors")

for i in range(attempts):
    user = input(f"\nRound {i+1} - Your choice: ").lower()
    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a draw!")
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        print("You win this round!")
        score += 1
    elif user in options:
        print("You lose this round!")
    else:
        print("Invalid input! No points this round.")

print("\nGame Over!")
print("Your total score out of 3:", score)
