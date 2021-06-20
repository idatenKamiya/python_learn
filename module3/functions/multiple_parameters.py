#add multiple parameters to a function by separating with a comma(,)

# Add a parameter to print_hand
def print_hand(hand, name):
    # Change the output to '___ picked: ___'
    print(name + ' picked: ' + hand)

# Add a second argument to print_hand
print_hand('Rock', 'Dan')

# Add a second argument to print_hand
print_hand('Paper', 'Computer')