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
