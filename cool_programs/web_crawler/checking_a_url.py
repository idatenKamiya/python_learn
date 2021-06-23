from urllib.request import urlopen

with urlopen("URL") as response:
    for line in response:
        print(line)