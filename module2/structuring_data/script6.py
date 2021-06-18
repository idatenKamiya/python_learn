#Loop through DICTIONARIES
#Use a 'for' loop to iterate through a dictionary by syntax: for variable_name in dictionary_name:
#'key' is the temporary variable using which you get the corresponding 'value' in  the dictionary.

fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'green'}
for fruit_key in fruits:
    print('The ' + fruit_key + ' is ' + fruits[fruit_key])

""" output >>>  The apple is red 
                The banana is yellow
                The grape is purple """   
