import random

'''
0 = Rock
1 = Paper
-1 = Scissors
'''

# Dictionaries for mapping
moves = {"r": 0, "p": 1, "s": -1}
reverse_moves = {0: "Rock", 1: "Paper", -1: "Scissors"}

# Random move by computer
computer = random.choice([0, 1, -1])

# User input
user = input("Enter your move (r for Rock, p for Paper, s for Scissors): ").lower()

# Check for invalid input
if user not in moves:
    print("❌ Invalid input! Please choose r, p, or s.")
else:
    user_input = moves[user]

    # Show moves
    print(f"🧑 You chose: {reverse_moves[user_input]}")
    print(f"💻 Computer chose: {reverse_moves[computer]}")

    # Game logic
    if user_input == computer:
        print("🤝 It's a draw!")

    elif (
        (user_input == 0 and computer == -1) or
        (user_input == 1 and computer == 0) or
        (user_input == -1 and computer == 1)
    ):
        print("✅ You win!")

    else:
        print("❌ You lose!")
