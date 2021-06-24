# The * operator unpacks the lists into individual elements

l1 = [1, 2, 3]
l2 = [4, 5, 6]
t = (*l1, *l2)
print(t)

#result: (1, 2, 3, 4, 5, 6)

#unpacking tuples comes in very handy when returning multiple values from a function
'''
#This program does not compile
def get_user_by_id(userid):
    # fetch user from database
    # ....
    return name, age
  
name, age = get_user_by_id(4)
'''