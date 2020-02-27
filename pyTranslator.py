import string
import time


################### FUNCTIONS ###################

def mainMenu():
    menu_question = input('START?  (y/n)  ')
    print('')
    if menu_question == ('y'):
        setupMenu()
    else:
        mainMenu()
    
def setupMenu():
    print('1. Reverse text')
    print('')
    print('2. Alphabet to binary')
    print('')
    print('')
    print('')
    print('        *Use only numbers')
    print('')
    choose_trans = input('Please choose a mode:  ')

    if choose_trans == ('1'):
        reverse()
    if choose_trans == ('2'):
        toBinary()

def reverse():
    time.sleep(1)
    print('')
    reverseInput = input(str('Insert text to revert:  '))
    print(reverseInput[::-1])
    print('')

    while input:
        True
        reverseInput = input(str('Insert text to revert:  '))
        print(reverseInput[::-1])
        continue

def toBinary():
    time.sleep(1)
    print('')
    binInput = input("Convert your text to binary: ")
    print(' '.join(format(ord(x), 'b') for x in binInput))
    print('')

    while input:
        True
        binInput = input("Convert your text to binary: ")
        print(' '.join(format(ord(x), 'b') for x in binInput))
        continue
################### FUNCTIONS ###################

print('')
print('T R A N S L A T O R')
print('')
time.sleep(1)
mainMenu()
