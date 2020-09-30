"""A number-guessing game."""

# Put your code here
import random
#greet player
print("Hi There")
#get player name
name = input('What is your name? ')
#choose random number between 1 and 100
correct_num = random.randint(1,100)
#repeat forever:
    # get guess
    # if guess is incorrect:
    #     give hint
    #     increase number of guesses
    # else:
    #     congratulate player
guesses = 1

while True: 
    guess = int(input('What number would you like to guess? '))
    if guess == correct_num:
        print (f'Congratulations! You guessed it in {guesses} tries')
        break
    elif guess > 100:
        print("Way too high, the number is from 1-100, try again")
        guesses += 1
    elif guess < correct_num: 
        print('too low, try again')
        guesses += 1
    elif guess > correct_num:
        print('too high, try again')
        guesses += 1
