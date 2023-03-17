import random #importing random built in library so that i can create a variable with random numbers
#making a function
def game(player):

    print("Great choice!\n")

    players_choice_lower = player.lower()

    # comparison and assigning
    if players_choice_lower == "rock":
        player = rock
    elif players_choice_lower == "paper":
        player = paper
    elif players_choice_lower == "scissors":
        player = scissors
    else:
        raise SystemExit("Invalid input. Try again...")

    # creating a variable with random numbers
    computer_choice = random.randint(1, 3)
    # creating a string with no characters in it, so that we can assign information to it later after
    # finding what is the chosen number by the computer
    computer_move = ''

    if computer_choice == 1:
        computer_move = rock
    elif computer_choice == 2:
        computer_move = paper
    elif computer_choice == 3:
        computer_move = scissors

    print(f"The computer has chosen {computer_move}")

    # comparing so that the program can see who is the winner
    if (player == rock and computer_move == scissors) or \
            (player == scissors and computer_move == paper) or \
            (player == paper and computer_move == rock):
        print("The computer has taken a big L...\n")
        print("Congratulations, you win!")
        

    elif player == computer_move:
        print("Oh...it's a draw")
    else:
        print("Ha-ha, you've taken the big L\nLoser!")



print("Hello! My name is PC!\n")
print("Let's play a game of Rock-Paper-Scissors!\n")


rock = "rock"
paper = "paper"
scissors = "scissors"

players_choice = input("Choose one of the following - Rock, Paper or Scissors:\n")
game(players_choice,counter_player,counter_pc) #calling game function

dunno = input("Do you want to continue playing this game?\n")

while dunno.lower == 'yes': #i made it == 'yes', so that it will be guaranteed that the user wants to play
    players_choice = input("Choose one of the following - Rock, Paper or Scissors:\n")

    game(players_choice)

    dunno = input("Do you want to continue playing this game?\n")





