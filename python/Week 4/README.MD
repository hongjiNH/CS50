#  emojize
```
import emoji
user_input = input("Input: ")
print(f"Output: {emoji.emojize(user_input,language="alias")}")

```
# figlet
```
import pyfiglet
import sys

try:
    if len(sys.argv)==3 and (sys.argv[1] =="-f" or sys.argv[1] =="--font"):
        pyfiglet.figlet_format("test",font=sys.argv[2])
        user_input = input("Input: ").strip()
        print(f"Output:\n {pyfiglet.figlet_format(user_input,font=sys.argv[2])}")
    else:
        if len(sys.argv)==1:
            user_input = input("Input: ").strip()
            print(f"Output:\n {pyfiglet.figlet_format(user_input)}")
        else:
            sys.exit("Invalid usage")

except:
    sys.exit("Invalid usage")
```
# adieu
```
from inflect import engine

names = []

def print_names(names):

    result = engine().join(tuple(names))
    print(f"Adieu, adieu, to {result}")

while True:
    try:
        user_input = input("Name: ").strip()
        if (user_input == ""):
            print_names(user_input)
            break
        names.append(user_input)
    except EOFError:
        print_names(names)
        break

```
# game
```
from random import randint

while True:
    try:
        level = int(input("Level: "))
        random_number = randint(1, level)
        while True:

            user_input = int(input("Guess: "))
            if (user_input > random_number):
                print("Too large!")
            elif (user_input < random_number):
                print("Too small!")
            else:
                print("Just right!")
                break
        break
    except ValueError:
        continue

```
# professor
```
from random import randint

def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x,y = generate_integer(level), generate_integer(level)

        for tries in range(3):
            try:
                user_input=int(input(f"{x} + {y} = "))
                if user_input == x + y:
                    score +=1
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")
            if (tries == 2):
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if (level == 1):
        return randint(0, 9)
    elif (level == 2):
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()

```
# bitcoin
```
import requests
import sys

if (len(sys.argv) < 2):
    sys.exit("Missing command-line argument")

if sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")

try:
    res = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=YOURAPIKEY').json()
    cost = float(res['data']['priceUsd']) * float(sys.argv[1])
    output = "$"+"{:,.4f}".format(cost)

    print(output)

except requests.RequestException:
    print("idk what to type here")

```
