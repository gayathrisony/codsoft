from random import choice
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def play(user_choice):
    computer_choice = choice(["rock", "paper", "scissors"])
    
    print("\nYour choice:\n")
    if user_choice == "rock":
        print(rock)
    elif user_choice == "paper":
        print(paper)
    else:
        print(scissors)

    print("\nComputer's choice:\n")
    if computer_choice == "rock":
        print(rock)
    elif computer_choice == "paper":
        print(paper)
    else:
        print(scissors)
    
    time.sleep(1)  # Add delay for dramatic effect
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

user_wins = 0
computer_wins = 0

for _ in range(3):
    user_choice = input("Choose: Rock, Paper, or Scissors: ").lower()

    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose: Rock, Paper, or Scissors.")
        user_choice = input("Choose: Rock, Paper, or Scissors: ").lower()

    result = play(user_choice)
    print("\n" + result)

    if "win" in result.lower():
        user_wins += 1
    elif "lose" in result.lower():
        computer_wins += 1

print("\nGame Over!")
if user_wins > computer_wins:
    print("You win the game!")
elif user_wins < computer_wins:
    print("Computer wins the game!")
else:
    print("It's a tie game!")
