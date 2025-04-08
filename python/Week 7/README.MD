#  numb3rs
```
from re import search

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    temp = "(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    if search("^" + r"\.".join([temp] * 4) + "$",ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

```
test_numb3rs
```
from numb3rs import validate

def test_numb3rs():
    assert validate("64.128.256.512") == False
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False

def test_validate_first_byte():
    assert validate("300.69.69.69") == False
    assert validate("1.420.69.0") == False

```
# watch
```
import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'^.*iframe src=\"(?:https?://)?(?:www\.)?youtube\.com/(?:embed/)?([a-zA-Z0-9_-]{11})\".*$', s, re.IGNORECASE)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()

```
# working
```
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

```
test_working
```
import pytest
from working import convert

def test_validate_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("9:00 PM to 5:30 AM") == "21:00 to 05:30"

def test_value_error_to():
    with pytest.raises(ValueError):
        assert convert("9:00 AM lol 5:30 PM")

def test_value_error_range():
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 69:30 PM")


```
# um
```
import re

def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"\bum\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()

```
test_um
```
from um import count

def test_um():
    assert count("um, lol, UM lol") == 2
    assert count("um, yummmmy") == 1


```
# response
```
import validators

user_input = input("What's your email address? ")

if validators.email(user_input):
    print("Valid")
else:
    print("Invalid")


```
