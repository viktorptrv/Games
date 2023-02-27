import random #importing random built in library so that i can create a variable with random numbers

print("Hello! My name is PC!\n")
print("Let's play a game of Rock-Paper-Scissors!\n")

players_choice = input("Choose one of the following - Rock, Paper or Scissors:\n")

print("Great choice!\n")

players_choice_lower = players_choice.lower()

rock = "rock"
paper = "paper"
scissors = "scissors"

# comparison and assigning
if players_choice_lower == "rock":
    player_choice = rock
elif players_choice_lower == "paper":
    players_choice = paper
elif players_choice_lower == "scissors":
    players_choice = scissors
else:
    raise SystemExit("Invalid input. Try again...")

# creating a variable with random numbers
computer_choice = random.randint(1,3)
# creating a string with no characters in it, so that we can assign information to it later after
# finding what is the chosen number by the computer
computer_move = ''

if computer_choice ==  1:
    computer_move = rock
elif computer_choice == 2:
    computer_move = paper
elif computer_choice == 3:
    computer_move = scissors

print(f"The computer has chosen {computer_move}")

#comparing so that the program can see who is the winner
if (players_choice == rock and computer_move == scissors) or \
        (players_choice == scissors and computer_move == paper) or \
        (players_choice == paper and computer_move == rock):
    print("The computer has taken a big L...\n")
    print("Congratulations, you win!")
elif players_choice == computer_move:
    print("Oh...it's a draw")
else:
    print("Ha-ha, you've taken the big L\nLoser!")