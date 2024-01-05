from random_word import RandomWords


def user_letter():
    letter: str = input("Enter a letter: ")
    return letter


tries = 0
r = RandomWords()
word = r.get_random_word()

word_list = [i for i in word]
word_list_underscore = ['_' for i in range(len(word_list))]

while True:
    user_chosen_letter = user_letter()

    if user_chosen_letter.isalpha():
        if user_chosen_letter in word_list:
            for i in word_list:
                if i == user_chosen_letter:
                    index = word_list.index(i)
                    word_list_underscore.pop(index)
                    word_list_underscore.insert(index, user_chosen_letter)
            print(''.join(str(i) for i in word_list_underscore))
            if "_" not in word_list_underscore:
                print("YOU WON!")
                break
        else:
            tries += 1
            if tries < 3:
                print(f"You have {3-tries} tries left!")
            else:
                print("You are done, BB")
                break
    else:
        print("Choose a letter!!!!!")
        continue
