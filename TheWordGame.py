import random
# make later
# def generator(word): #function for generator
# def comparison: #function for comparing
count = 0
word_dictionary = {'intend': 'have in mind as a purpose',
                   'concern': 'something that interests you because it is important',
                   'commit': 'perform an act, usually with a negative connotation',
                   'issue': 'some situation or event that is thought about',
                   'approach': 'move towards', 'establish': 'set up or found',
                   'engage': 'consume all of ones attention or time',
                   'obtain': 'come into possession of',
                   'scarce': 'deficient in quantity or number compared with the demand',
                   'straight': 'successive, without a break',
                   'stock': 'capital raised by a corporation through the issue of shares',
                   'fancy': 'imagine', 'court': 'an assembly to conduct judicial business'}

print('Hello there! Do you want to play a game of Guess the Word?')
yes_or_no = input()

if yes_or_no.lower() == 'yes':
    print('Awesome, lets start then!')

print('Those are all words in my dictionary :) choose carefully')
for k in word_dictionary.keys():
    print(f"{k}", end='/ ')

# make it a function later
# the program chooses random word from the dictionary
key, value = random.choice(list(word_dictionary.items()))  # value is going to be used later
key_index = int(list(word_dictionary).index(key))
user_input = input('\nYour choice is: ')
print('Perfect choice!')

if user_input == key:
    print("Wow you guessed it!")
    print("But can you guess its meaning?")
    for values in word_dictionary.values():
        print(f'{count}. {values}')
        count += 1
    print(f'Choose which line is the meaning of the word {key}:')
    user_line = int(input())

    if user_line == key_index:
        print("Bingo!")
    else:
        print('Too bad! LOOOOOOSEEEERRRR !!!!!')
else:
    print("But sadly, its not the right one...BYE BYE LOOSER")
    print('Ok ok i will give you another try\nThis is a hint... its one of the following words:')
    for i in word_dictionary.keys():
        if list(word_dictionary.keys()).index(i) in range(max(0, key_index-2), key_index+2):
            print(i)
    user_input = input()

    # function later
    if user_input == key:
        print("Wow you guessed it!")
        print("But can you guess its meaning?")
        for values in word_dictionary.values():
            print(f'{count}. {values}')
            count += 1
        print(f'Choose which line is the meaning of the word {key}:')
        user_line = int(input())

        if user_line == key_index:
            print("Bingo!")
        else:
            print('Too bad! LOOOOOOSEEEERRRR !!!!!')
    else:
        print('Wow what a loser you are! Its over!!!')


