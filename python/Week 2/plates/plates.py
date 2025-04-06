import re

def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if re.match("^(?=.{2,6}$)[A-Za-z]{2,}[1-9][0-9]*$|^(?=.{2,6}$)[A-Za-z]{2,}$",s):
        return True
    else:
        return False



main()
