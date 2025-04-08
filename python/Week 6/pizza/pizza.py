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
