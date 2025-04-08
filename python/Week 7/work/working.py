from re import search, findall

def main():
    print(convert(input("Hours: ")))


def convert(s):
    temp = "(1[0-2]|[1-9]):?([0-5][0-9])?"
    pattern = "^" + temp + " (AM|PM) to " + temp + " (AM|PM)$"
    matches = search(pattern,s)
    if matches:

        first_number, sec_number= matches.group(1), matches.group(2) or "00"
        third_number, forth_number = matches.group(4), matches.group(5) or "00"

        if  matches.group(3) =="PM" and int(matches.group(1)) !=12:
            first_number = int(matches.group(1)) +12

        if  matches.group(3) =="AM" and int(matches.group(1)) <10:
            first_number = f"0{matches.group(1)}"

        if  matches.group(3) =="AM" and int(matches.group(1)) ==12:
            first_number = "00"

        if matches.group(6) =="PM"  and int(matches.group(4)) !=12:
            third_number = int(matches.group(4)) +12

        if  matches.group(6) =="AM" and int(matches.group(4)) ==12:
            third_number = "00"

        if  matches.group(6) =="AM" and int(matches.group(4)) <10:
            third_number = f"0{matches.group(4)}"

        return f"{first_number}:{sec_number} to {third_number}:{forth_number}"
    else:
        raise ValueError("lol")

if __name__ == "__main__":
    main()
