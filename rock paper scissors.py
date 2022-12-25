# Random guess from system

import random

system_hand = random.randint(0,2)

# Define all the possibilities
# Define possibilities for winning or loosing

r = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

p = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

s = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

# 1 = ROCK, 2 = PAPER, 3= SCISSOR
def game():
    print('''$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/ ''')
    print("Let's play rock paper scissor!")
    hands = [r,p,s]
    user_input = int(input('I choose:'))
    print(f'You choose: {hands[user_input]}')
    if system_hand == 0 and user_input == 1:
        print(f'You won because system chose {hands[system_hand]}!')
    elif system_hand == 1 and user_input == 2:
        print(f'You won because the system chose {hands[system_hand]}')
    elif system_hand == 2 and user_input == 0:
        print(f'You won because the system chose {hands[system_hand]}')
    elif system_hand == user_input:
        print(f'Its a tie because you both choose: {hands[user_input]}')
    else:
        print(f'System won because it chose {hands[system_hand]}')

game()