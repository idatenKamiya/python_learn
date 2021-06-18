#break statement - Used to exit the loop immediately when the condition is met.
#Usually combined with if statements.

#example1:
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    print(number)
    if number == 3:
        break
"""output >>>   1
                2
                3 """

#example2:
numbers = [123, 895, 555, 258]
for number in numbers:
    print(number)
    # When the number variable is 777, print '777 found, stopping loop' and exit the loop
    if number == 555:
        print('555 found, stopping loop')
        break   
"""output >>>   123
                895
                555
                555 found, stopping loop """