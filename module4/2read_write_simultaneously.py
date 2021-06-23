with open('text.txt', 'r') as in_file:
    with open('output.txt', 'w') as out_file:
        for line in in_file.readlines():
            out_file.write(line)