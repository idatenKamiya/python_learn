#parameters are defined in the functions
#arguments are the values passed while calling the function.

#example1:
'''def greet(name):
    print('Hello ' + name)

greet('John')
greet('Kate')'''

#example2:

# Add a parameter to print_hand
def print_hand(hand):
    # Use the parameter to print 'You picked: ___'
    print('You picked: ' + hand)

# Call print_hand with 'Rock'
print_hand('Rock')

# Call print_hand with 'Paper'
print_hand('Paper')