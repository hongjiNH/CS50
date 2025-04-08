#  lines
```
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].lower().endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        lines_of_code = 0
        for line in file:
            line = line.strip()
            if not line.startswith("#") and line != "":
                lines_of_code += 1
        print(lines_of_code)
except FileNotFoundError:
    sys.exit("File does not exist")

```
# pizza
```
import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arugments")

if not sys.argv[1].lower().endswith(".csv"):
    sys.exit("Not a CSV File")

table =[]
header = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            value = list(row.values())
            table.append(value)


    print(tabulate(table,headers=header, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")

```
# scourgify
```
import sys
import csv

if (len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
elif (len(sys.argv) > 3):
    sys.exit("Too many command-line arugments")

input_csv_file, output_csv_file = sys.argv[1:]
if not input_csv_file.endswith(".csv"):
    sys.exit("Not a CSV File")

output=[]
try:
    with open(input_csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].split(", ")
            output.append({"first": first, "last": last, "house": row["house"]})

    with open(output_csv_file, 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(output)

except FileNotFoundError:
    sys.exit(f"Could not read {input_csv_file}")


```
# shirt
```
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


```
