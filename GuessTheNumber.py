import random


def play_the_game(count):
    while True:
        user = user_numbers()
        count += 1
        if isinstance(user, int):
            if user < number:
                print("Chosen number is smaller")
            elif user > number:
                print("Chosen number is bigger")
            else:
                print("Jackpot!")
                return count


def user_inputs():
    user_input: str = input("Do you wanna play the 'Guess the Number' game?")
    return user_input


def user_numbers():
    user_number: int = int(input('Guess:'))
    return user_number


count = 0
while True:
    user_input_ans = user_inputs().lower()

    if user_input_ans in ['y', 'yes', 'ye']:
        number = random.randint(0, 10)
        print(f"You won in {play_the_game(count)} try/ies!")
        if input("Wanna try again? ") in ['n', 'no', 'nah']:
            print("Ok BB")
            continue
        break

    elif user_input_ans in ['n', 'no', 'nah']:
        print("Ok BB")
        break

    else:
        print("Please type a number")
        continue


