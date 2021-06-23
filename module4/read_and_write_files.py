#read and write

with open('text.txt', 'r+') as f:
    for line in f:
         print(line.strip())
    f.write("The End!")



