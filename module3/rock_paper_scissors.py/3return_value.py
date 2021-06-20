#the program gives an error for values outside (0,1,2). we need to validate this.
#Let deal with it using 'return' value

# Define the validate function
def validate(hand):
    # Add control flow based on the value hand
    if hand < 0 or hand > 2:
        return False
    #can be rewritten without the else statement and reindenting the 'return true' line    
    else:                       
        return True
    
def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ')

print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Please enter a number (0-2): '))

# Add control flow based on the return value of the validate function
if validate(player_hand):
    print_hand(player_hand, player_name)
else:
    print('Please enter a valid number')


#return statement not only sends back the return value to the caller, it also stops the function immediately.
#anything after 'return' will not be executed