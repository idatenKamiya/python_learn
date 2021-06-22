#a simple game to guess a number between 1-100
#the number to guess is completelty random
#check out the try-except format to stop the game from crashing


from random import randint

num = randint(1, 100)
num_of_tries = 0
print("Welcome to the number guessing game!")

while True:
    #get input
    try:
        guess + int(input("What number am I thinking of? (1-100 or 0 to exit): "))
        num_of_tries += 1
    except:
        print("Please input a number 1-100!")
        continue

    if guess == 0:
        break
    elif guess < 1 or guess > 100:
        print("Please input a number 1-100!")
    else:
        if num == guess:
            print("You won in " + str(num_of_tries) + " tries!")
            again = input("Would you like to play again? Enter 'Y' for yes, and anything else to quit")
            if again == 'Y' or again =='y':
                num = randint(1, 100)
                num_of_tries = 0
            else:
                break
        else:
            if num > guess:
                print("Too low, try again. ")
            else:
                print("Too high, try again.")

print("Thhanks for playing, hope to see you soon!")