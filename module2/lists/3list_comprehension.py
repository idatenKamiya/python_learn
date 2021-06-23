#List comprehension

#exaple1:
'''
threes = []
for i in range(1, 20):
    if i % 3 == 0:
        threes.append(i)
print(threes)
'''
#------------------------------------
#make a simple list comprehension
'''
threes = [i for i in range(1, 20)]
print(threes)
'''
#------------------------------------

#add the condition
'''
threes = [i for i in range(1, 20) if i % 3 == 0]
print(threes)     #gives the same result as the first example
'''
#####################################################################

#example2: work with powers
powers = [2**i for i in range(1, 10)]
print(powers)
