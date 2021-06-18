#Dictionaries are used to manage groups of data. (like LIST's)
#(But differs from a List) dictionaries use keys instead of index numbers.
#In Dictionaries, a key is paired with a value (key-value pair) to form one element.

#Syntax: variable_name = {key1: value1, key2: value2, ..}

fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'green'}
print(fruits)
#output >>> {'banana': 'yellow', 'apple': 'red', 'grape': 'green'} ***Notice the order is different***


#You can get a value from a dictionary using the key, by writing dictionary_name[key]
fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'green'}
print('The banana is ' + fruits['banana'])