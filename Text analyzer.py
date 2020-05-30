import re
from collections import Counter

'''
author = Ekaterina Voropaeva
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
         ]

username_password = {'bob': '123',
                     'ann': 'pass123',
                     'mike': 'password123',
                     'liz': 'pass123'}
border = '-' * 39
print(f'{border}\nWelcome to the app. Please log in: \n{border}')
user = input('USERNAME: ')
pwd = input('PASSWORD: ')
print(border)

if user in username_password.keys() and pwd == username_password[user]:
    print('Logged on')
else:
    print('Wrong credentials')
    exit()

print(f'{border}\nWe have 3 texts to be analyzed.\n')
text_choice = int(input('Enter a number btw. 1 to 3 to select: '))
print(border)

chosen_text = ''

if text_choice == 1:
    chosen_text = TEXTS[0]

elif text_choice == 2:
    chosen_text = TEXTS[1]

elif text_choice == 3:
    chosen_text = TEXTS[2]

simple_words = chosen_text.split()

for word in simple_words:
    clear_wrd = word.strip('.,/')

counter = 0
for word in simple_words:
    if word.istitle():
        counter += 1
print(f'There are {counter} titlecase words.')

counter = 0
for word in simple_words:
    if word.isupper():
        counter += 1
print(f'There are {counter} uppercase words.')

counter = 0
for word in simple_words:
    if word.islower():
        counter += 1
print(f'There are {counter} lowercase words.')

counter = 0
for word in simple_words:
    if word.isdigit():
        counter += 1
print(f'There are {counter} numeric strings.')

# use asterix as number of letters
asterisk_words = []
for word in simple_words:
    asterisk = '*' * len(word)
    asterisk_words.append(asterisk)

sorted_words = sorted(asterisk_words, key=len)

counted_words = Counter(sorted_words)

for key, value in counted_words.items():
    print(f'Found {value} word(s): with {key} {len(key)} letter(s)')
    # asterix as number of found words
    # asterix_words_number = '*' * value
    # print(f'{len(key)} {asterix_words_number} {value}')

summ = 0
for word in simple_words:
    if word.isdigit():
        summ += int(word)
print(f'{border}\nIf we summed all the numbers in this text we would get: {summ}\n{border}')
