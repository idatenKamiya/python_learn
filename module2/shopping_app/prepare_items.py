#refer buy_apple.py in the repo for the simple logic of ordering items
#Let's improve the app.
#we'll print results according to the number of items order by customer (through input in the console)

"""1. Prepare a dictionary of fruits or vegetables or any class of items you like 
   2. Example here has a dictionary of fruits with fruit names as 'key' and prices as 'values'
   3. We'll print the price of each fruit using loops """

# Create a dictionary with keys and values, and assign it to the items variable
items = {'apple': 2, 'banana': 4, 'orange': 6}
# Create a for loop that gets the keys of items
for item_name in items:
    print('-----------------------------------------------')
    # Print 'Each ___ costs ___ dollars'
    print('Each ' + item_name + ' costs ' + str(items[item_name]) + ' dollars')


