import random

# Getting a random number
def guess_the_no():
    magic_no= random.randint(0,100)

    for i in range(5):
        guess= int(input('Guess the no: '))
        if magic_no == guess:
            print("You won! Congrats!")
        elif guess < magic_no:
            print("Hint! Go UP!!!")
        else:
            print("Hint! GO DOWN!!!")
        last_guess_value = guess
    print("The magic no was ", magic_no)
    if last_guess_value == magic_no:
        print("You Won!")
    else:
        print("You were just", abs(magic_no - last_guess_value), " no away from the magi no.")
        print("Better luck next time!")


guess_the_no()