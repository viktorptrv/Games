#making dictionary full of questions and answers
quiz_dictionary = {'What does “www” stand for in a website browser?': 'World Wide Web',
                   'How long is an Olympic swimming pool (in meters)?': '50 meters',
                   'What countries made up the original Axis powers in World War II?': 'Germany, Italy, and Japan',
                   'Which country do cities of Perth, Adelade & Brisbane belong to?': 'Australia',
                   'What geometric shape is generally used for stop signs?': 'Octagon',
                   'What is "cynophobia"?': 'Fear of dogs',
                   'What punctuation mark ends an imperative sentence?': 'period or exclamation point',
                   'Who named the Pacific Ocean?': 'Ferdinand Magellan',
                   'How many languages are written from right to left?': '12',
                   'What is the name of the biggest technology company in South Korea?': 'Samsung'}

#making a dictionary with the same keys but with false answers
false_answers_dictionary = {'What does “www” stand for in a website browser?':['world working web', 'wide world web'],
                            'How long is an Olympic swimming pool (in meters)?': ['100 meters','1000 meters'],
                            'What countries made up the original Axis powers in World War II?': ['Germany, France and England', 'Italy, England, Germany'],
                            'Which country do cities of Perth, Adelade & Brisbane belong to?': ['The USA','Europe'],
                            'What geometric shape is generally used for stop signs?': ['Triangle', 'Square'],
                            'What is "cynophobia"?': ['Fear of cats', 'Fear of pipes'],
                            'What punctuation mark ends an imperative sentence?': ['period or dot', 'only period'],
                            'Who named the Pacific Ocean?': ['Schwarzenegger','Ali Baba'],
                            'How many languages are written from right to left?': ['15', '21'],
                            'What is the name of the biggest technology company in South Korea?': ['Huawei','Sony']}

points = 0

print('Hello there! Do you want to play the Quiz Game?')
yes_no = input()

if yes_no.lower() == 'yes':
    print('Awesome! Lets start then!')
else:
    raise SystemExit("Well...ok, bye!")

print('You have to always give a right answer to the questions, else... you will see. Answers are not case sensitive.')

#making a for loop with the length of the dictionary

for i in range(len(quiz_dictionary)):
    for key in quiz_dictionary.keys():
        print('Current question is:')
        print(key)
        print('Choose one of the following answers:')
        print(quiz_dictionary[key])

        if key in false_answers_dictionary:
            print('\n'.join(false_answers_dictionary[key]))
        user_answer = input().lower()

        if user_answer == quiz_dictionary[key].lower():
            print('\nAwesome! You receive 1 point\n')
            points +=1
        else:
            print("\nF\n")

print(f"You finished the game with {points} points.")
if points < 8:
    print('Sadly you are a loser')
else:
    print('GG WP, you beat the game')



#ideas for later:
#make the correct answer take different lines every time

