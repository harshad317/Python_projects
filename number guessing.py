# Select a random no

import random

def no_to_guess():
    return random.randint(1,100)

# Guess the no and get the feedback from the system if the no guessed is correct or not.
# If the guessed no is not correct then give hint to the user and cut 25 points from 100 everytime the user could not guess the no.

def user_input(guess):
    guessed_numbers = []
    closest = []
    total_points = 100
    print('Your points are 100.')
    for i in range(0,100, 20):
        my_guess = int(input('I think the no is: '))
        guessed_numbers.append(my_guess)
        if my_guess == guess:
            return 'Well done!'
        if my_guess > guess:
            print('Pss...go down!')
            print('I am reducing 25 points for the hint!')
            total_points = total_points - 25
            print(f'You can still make {total_points} points')
            i +=25
        elif my_guess < guess:
            print('Pss...go up!')
            print('I am reducing 25 points for the hint!')
            total_points = total_points - 25
            print(f'You can still make {total_points} points')
            i += 25
    print(f'The real number was: {guess}')
    print(f'All of your guesses are: {guessed_numbers}')
    for i in guessed_numbers:
        closest.append(abs(guess - i))
    print(f'You only missed by: {min(closest)}.')

if __name__== '__main__':
    my = no_to_guess()
    user_input(my)