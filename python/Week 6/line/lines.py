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
