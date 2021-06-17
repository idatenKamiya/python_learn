#UPDATE and ADD elements to DICTIONARIES

#Updating the value of an existing key can be done by writing dictionary_name[key] = value
fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'green'}
fruits['apple'] = 'green' #<====== UPDATE the value

print('The apple is ' + fruits['apple'])
#output >>> The apple is green


#ADDING an element can be done by the same syntax as UPDATING.
#If the specified 'key' does not exist, new element with the key will be added.
fruits = {'apple': 'red', 'banana': 'yellow', 'grape': 'green'}
fruits['dragonfruit'] = 'pink'

print(fruits)
#output >>> {'dragonfruit': 'pink', 'apple': 'red', 'banana': 'yellow', 'grape': 'green'}