from sys import argv,exit
from PIL import Image, ImageOps

def main():
    if (len(argv) < 3):
        exit("Too few command-line arguments")
    elif (len(argv) > 3):
        exit("Too many command-line arugments")
    else:
        if file_extension(1)!=file_extension(2):
            exit("Input and output have different extensions")

try:

    shirt = Image.open("shirt.png")
    before = Image.open(argv[1])

    size = shirt.size
    before = ImageOps.fit(before, size)
    before.paste(shirt, box = (0, 0), mask = shirt)
    before.save(argv[2], format=None)

except FileNotFoundError:
    exit(f"Input does not exist")

def file_extension(i):
    temp = argv[i].lower()
    if temp.endswith(".jpg") or temp.endswith(".jpeg") or temp.endswith(".png"):
        return argv[i].split(".")[1]
    else:
        exit("Invalid output")

main()
