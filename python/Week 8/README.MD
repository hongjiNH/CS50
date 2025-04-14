# seasons
```
from datetime import datetime, date
import sys
import inflect
import re

def main():
    user_input= input("Date of Birth: ")
    return diff(user_input)

def diff(user_date):
    try:
        p = inflect.engine()
        match= re.search("^(1[0-9]{3}|2[0-9]{3})-(1[0-2]|0[1-9])-(0[1-9]|1[0-9]|2[0-9]|3[0])$",user_date)
        if match:
            user_yr, user_month, user_date = map(int, match.group().split("-"))

            today = date.today()
            dob_date = date(user_yr, user_month, user_date)

            days = abs((today - dob_date).days)

            minutes = days * 1440
            print(p.number_to_words(minutes, andword="").capitalize() + " minutes")
        else:
            raise ValueError
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()

```
test_seasons
```
import pytest
from seasons import diff

def test():

    with pytest.raises(SystemExit, match="Invalid"):
        diff("Januar 6th, 1998")
```
# jar
```
import sys

class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError
        self.cookies = 0


    def __str__(self):
        return "🍪"*self.cookies

    def deposit(self, n):
        if n+self.cookies <= self.capacity:
            self.cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self.cookies:
            self.cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

def main():
    print(Jar())

if __name__=='__main__':
    main()

```
test_jar
```
from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
         jar = Jar(-1)


def test_init_correct():
    jar = Jar(10)
    assert str(jar) == ''


def test_str():
    jar = Jar()
    assert str(jar) == ''

    jar.deposit(1)
    assert str(jar) == '🍪'


def test_deposit():
    jar = Jar(10)

    jar.deposit(10)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪'

    with pytest.raises(ValueError):
         jar.deposit(1)


```

# shirtficate
```
from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 45)
pdf.cell(0, 60, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0, y=70)
pdf.set_font_size(30)
pdf.set_text_color(255,255,255)
pdf.text(x=45, y=140, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")


```
