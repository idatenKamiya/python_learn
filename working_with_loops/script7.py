#while loops are used to repeat blocks of code until a given condition.
#syntax: while<conditional expression>:

#example:1
x = 1
while x <= 100:     #(x <= 100) is the conditional expression
    print(x)        #Keep running the code 'while' the condition is true

    x += 1          #increment-The value of x increases by 1 every time the code loops

"""Do not forget to the increment as it will lead to an infinite loop""" 
"""Do not forget to indent the increment as it will lead to an infinite loop""" 



#example:2
x = 10

# Create a while loop that repeats while x is greater than 0
while x > 0:
    # Print the x variable 
    print(x)
    # Subtract 1 from the x variable
    x -= 1