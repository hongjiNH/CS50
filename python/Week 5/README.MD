#  test_twttr
```
from twttr import shorten

def test():
    assert shorten("hmma")=="hmm"
    assert shorten("sequoia")=="sq"
    assert shorten("rhythm1")=="rhythm1"
    assert shorten("H,ELLO")=="H,LL"

```
twttr
```
def main():
    user_input = input("Input: ").strip()
    print(shorten(user_input))

def shorten(word):
    temp =""
    for inputs in word:
        if inputs.lower() == "a" or inputs.lower() == "e" or inputs.lower() == "i" or inputs.lower() == "o" or inputs.lower() == "u":
            temp = temp
        else:
            temp += inputs
    return temp


if __name__ == "__main__":
    main()

```
# test_bank
```
from bank import value

def test():
    assert value("Hello") == 0
    assert value("OK") == 100
    assert value("Hammad") == 20

```
bank
```
def main():
    user_input = input("Greeting: ").lower().strip()
    print(f"${value(user_input)}")

def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

```
# test_plates
```
from plates import is_valid

def test_plates():
    assert is_valid("A2") == False
    assert is_valid("zu#kk") == False

def test_length():
    assert is_valid("AAAAAAA") == False

def test_number_placement():
     assert is_valid("cs50as") == False

def test_zero_placement():
    assert is_valid("CS05") == False

```
plate
```
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

if __name__ == "__main__":
    main()

```
# test)fuel
```
from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/100") == 1

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_labelingpercent():
    assert gauge(25) == "25%"

def test_labeling1():
    assert gauge(1) == "E"

def test_labeling99():
    assert gauge(99) == "F"

```
fuel
```
def main():
    user_input = input("Fraction: ")
    percentage =convert(user_input)
    print(gauge(percentage))

def convert(fraction):
    x, y = fraction.split("/")

    if y == "0":
        raise ZeroDivisionError
    if not x.isnumeric() or not y.isnumeric() or (int(x) > int(y)):
        raise ValueError

    x = int(x)
    y = int(y)
    return round((x/y)*100)

def gauge(percentage):
    if percentage <= 1:
           return "E"
    elif percentage>=99:
        if percentage >100:

        else:
            return "F"

if __name__ == "__main__":
    main()


```
