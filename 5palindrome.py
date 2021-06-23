#This program can be done in many ways. This is one of the beginner ways.
#Palindrome is a sequence that is the same forward and backwards
#palindrome is just a word that can be read forwards and backwards
#not mirror images


pal = "Malayalam"
pal = pal.lower()
start_index = 0
end_index = len(pal) - 1

while start_index <= end_index:
    if pal[start_index] != pal[end_index]:
        break
    start_index += 1
    end_index -= 1

if start_index >= end_index:
    print("It's a palindrome!")
else:
    print("Not a palindrome")
