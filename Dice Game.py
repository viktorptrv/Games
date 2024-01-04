import random


def user_input():
    user_numbers: str = input("How many dice would you like to roll? ")
    if user_numbers.lower() == 'exit':
        exit()
    return user_numbers


def rand_numbers(user_num):
    for i in range(user_num):
        num = random.randint(0, 10)
        numbers.append(num)
    return numbers


numbers = []

while True:
    user_input_numbers = int(user_input())
    print(' '.join(str(i) for i in rand_numbers(user_input_numbers)))
    numbers.clear()