#since our code becomes very long and difficult to read, its often a good practice to create modules.
#module is a file that can be imported into another file.
#move the functions to utils.py
#import a module with the syntax: import module_name
#no need to add .py when you import

#You can call a function of a module by putting the name of the module before the function name, like module_name.function_name()

#finally we can use the python standard library to get a random number and store it in computer_hand
#With 'random.randint(x, y)', you can get a random integer between x and y inclusive.

# import the utils module
import utils
import random

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

# Call the validate function of utils module
if utils.validate(player_hand):
    computer_hand = random.randint(0, 2)
    
    # Call the print_hand function of utils module
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')
    
    # Call the judge function of utils module
    result = utils.judge(player_hand, computer_hand)
    print('Result: ' + result)
else:
    print('Please enter a valid number')