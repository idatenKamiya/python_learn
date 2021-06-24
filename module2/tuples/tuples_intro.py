# It can hold multiple values in a single variable
# It’s ordered: the order of items is preserved
# A tuple can have duplicate values
# It’s indexed: you can access items numerically
# A tuple can have an arbitrary length

# A tuple is immutable; it can not be changed once you defined it.
# A tuple is defined using parentheses () instead of square brackets [] like in a list

my_numbers = (1, 2, 3)
my_strings = ('Hello', 'World')
my_mixed_tuple = ('Hello', 123, True)

print(my_numbers)
print(my_strings)
print(my_mixed_tuple)


 #A tuple can also be created by using the tuple() constructor from that class
list = [0,1,2] 
list.tuble()

#result: (0, 1, 2) 


#A tuple with just one item is useless for most use cases, but it demonstrates how Python recognizes a tuple. If you want to be absolutely certain that you are creating a tuple, you can always use the tuple() constructor
