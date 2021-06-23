# w-write (create)
# r-read

# creates a text file in your directory
with open("sample.txt", "w") as fw:
    fw.write("writing some stuff in my text file\n")
    fw.write("I like programming\n")


# reads the text file created above
with open("sample.txt", "r") as fr:
    text = fr.read()
    print(text)
