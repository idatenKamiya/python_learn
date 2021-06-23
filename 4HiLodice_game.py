#If you havent learnt functions yet

#A dice game which is going to be HIGH or LOW
#You are going to bet on HIGH or LOW or 7
#You will be rolling 2 dice
#You can quit if you have enough money or when you have lost all the money


from random import randint


cash = 100
bet = 5

while True:
    #The menu
    print("\n---------------------------------")
    print("Place your bet or enter X to exit")
    print("1) High roll of 8-12 for bet x2")
    print("2) Low  roll of 2-6 for bet x2")
    print("3) 7    roll        for bet x3")
    print("Cash on hand: " + str(cash))
    print("------------------------------------")
    choice = input("Make your choice: ")

    if choice == 'x' or choice == 'X':
        print("Thanks for playing and hope to see you back soon.")
        break

    #the game logic
    elif choice in ['1', '2', '3']:
        #betting loop
        while True:
            try:
                bet = int(input("Place your bet: "))
            except:
                print("Please enter a number")
                continue
            if bet > 0 and bet <= cash:
                break
            else:
                print("That bet is not valid")


        roll = randint(1, 6) + randint(1, 6)
        print("You rolled a: " + str(roll))

        if roll > 7 and choice == '1':
            print("You win!")
            cash = cash + bet               #1 and 2 conditions can be combined
        elif roll < 7 and choice == '2':
            print("You win!")
            cash = cash + bet
        elif roll == 7 and choice == '3':
            print("You win!")
            cash = cash + (2 * bet)
        else:
            print("You lose!")
            cash = cash - bet
            if cash == 0:
                print("You're out of money, see ya next time")
                break
    else:
        print("Enter a valid choice!")
        continue
