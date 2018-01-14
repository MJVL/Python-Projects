import random

randNum = random.randint(1,100)
numGuesses = 0
guess = -1

while guess != randNum:
    print('Enter your guess:')
    guess = int(input())
    numGuesses += 1
    if guess < randNum:
        print('Too low.')
    elif guess > randNum:
        print('Too high.')
    else:
        print('You guessed it, the correct number was ' + str(randNum) + '. It took you ' + str(numGuesses) + 'guesses.')

