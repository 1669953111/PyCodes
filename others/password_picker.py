import random
import string

adjs = ['sleepy', 'slow', 'smelly',
       'wet', 'fat', 'red',
       'orange', 'yellow', 'green',
       'blue', 'purple', 'fluffy',
       'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball',
         'toaster', 'goat', 'dragon',
         'hammer', 'duck', 'panda']

print("Welcome to Password Picker!")

while True:
    adj = random.choice(adjs)
    noun = random.choice(nouns)
    number = random.randrange(0, 100)
    special_char = random.choice(string.punctuation)
    # generate a password
    password = adj + noun + number + special_char
    print(f"Your new password is {password}")
    # other password?
    response = input("Would you like other password?[y/n]: ")
    if response == 'n':
        break