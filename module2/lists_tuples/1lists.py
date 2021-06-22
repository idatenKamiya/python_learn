#List is also known as an array (Java, C, C++....)
#Mutable means a list can change in length and type
#Immutable means a list stays the same length and type

#-------------------------------------------------------------------
#Index   0   1   2   3   4   5   6   7   8   9
ages1 = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15] #<- Elements

ages1[6] = 4.55 #add anything you want since it is a list and replace if index already has a value
print(ages1)

#-------------------------------------------------------------------
'''
ages1 = [14, 15, 13, 18, 14, 15, 16, 18, 17, 15]
ages2 = [15, 16, 17, 14]

#concatenation of lists
ages3 = ages1 + ages2
print(ages3)
'''
#--------------------------------------------------------------------
#You can also copy a list into itseld of add another list in it

'''
ages3 = ages * 2
'''
#--------------------------------------------------------------------
#you can pass a list inside these function:
#len(), min(), max(), sum() and the operators 'in and 'not in'
#--------------------------------------------------------------------
#list_name.append(value), list_name.insert(index, value), list_name.extend([values])

#list_name.pop() removes last value in list.
#list_name.pop(index) removes the value at the index
#list_name.remove(value) removes the value from the beginning of the list
#list_name.remove(index) removes at the index
#list_name.count(value) returns the number of times value is present in the list
#list_name.sort()
#list_name.reverse()