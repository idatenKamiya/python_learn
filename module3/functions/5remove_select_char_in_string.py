#Trying to remove characters in a string at the desired positions

def remove_mod(string, mod_val):
    new_string = ''
    for index in range(0, len(string)):
        if index % mod_val != 0:
            new_string = new_string + string[index]
        return new_string

a = remove_mod("This is my super awesome string!", 2)