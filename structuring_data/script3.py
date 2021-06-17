#When you want to print all the elements of a list, it's not efficient to repeat the same code like the example on the left.

#You can use a for loop to make it easier.


#without For loop:
foods = ['rasam', 'sambar', 'huli']
print('i like ' + foods[0])
print('i like ' + foods[1])
print('i like ' + foods[2])


#with For loop:
foods = ['rasam', 'sambar', 'huli']
for food in foods:
    print('i like ' + food)

#The for loop allows you to process each element of a list with a temporary variable, and apply the same code to it. 
#In the example above, each element of the foods variable is stored in a temporary variable called food, and printed.
#Iteration = Elements of the list will be assigned to the temporary variable one by one, and the code within the for loop gets executed with each assignment.    