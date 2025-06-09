# Ask the user to make a choice
# If choice is not valid
#  print an error
# Let the computer to make a choice
# print choice (emojis)
# Determine the winner
# Ask the user if they want to continue
# if not
# Terminate
import random

emojis = {"r": "🪨", "p": "📃", "s": "✂️"}
choices = ("r", "p", "s")
while True:
    user_choice = input("Rock, Paper, Scissor? (r/p/s): ").lower()
    # if user_choice != r and user_choice != p and user_choice != s:
    #     print("Invalid choice!")
    if user_choice not in choices:
        print("Invalid choices!")
        continue

    computer_choice = random.choice(choices)

    print(f"You choose {emojis[user_choice]}")
    print(f"Computer choose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    # elif user_choice == 'r' and computer_choice == 's':
    #     print('You win!')
    # elif user_choice == 's' and computer_choice == 'p':
    #     print('You win!')
    elif (
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "s" and computer_choice == "p")
        or (user_choice == "p" and computer_choice == "r")
    ):
        print("You win!")
    else:
        print("You lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == "n":
        break
