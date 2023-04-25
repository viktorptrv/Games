#Just a simple password generator using elements from the ASCII Table
import random

password = ''
banned_numbers = [40,41,38,34,44,58,59,93,91,94,96,46] #banned numbers and their characters

length = int(input('This is a password generator, how long do u want your password to be:\n'))

if length < 6:
    length = int(input('It cant be lower than 6 characters\n'))

for i in range(length):    

    #making a variable and assigning randon number to it from the ascii table
    random_number = random.randint(33, 122)
    
    if random_number in banned_numbers:
        while True:
            if random_number not in banned_numbers:
                break
            else:
                random_number = random.randint(33, 122)

    password += chr(random_number)

print(f'Your password is: {password}\nDont tell anybody!!!!!')
