# camel case 
```
user_input = input("camelCase: ")

def camel(user_input):
    temp = ""
    for inputs in user_input:
        if inputs.isupper():
            temp += "_" + inputs.lower()
        else:
            temp += inputs

    return temp

print(camel(user_input))


```
# coke
```
amount = 50

while amount >0:
    print("Amount Due:",amount)
    user_input = int(input("Insert Coin: "))

    if user_input ==25 or user_input == 10 or user_input ==5:
        amount -= user_input
        continue

if amount < 0:
    print("Change Owed:", amount*-1)
else:
    print("Change Owed:", amount)


```
# twitter
```
user_input = input("Input: ").strip()

def twitter(inputs):
    temp =""
    for inputs in user_input:
        if inputs.lower() == "a" or inputs.lower() == "e" or inputs.lower() == "i" or inputs.lower() == "o" or inputs.lower() == "u":
            temp = temp
        else:
            temp += inputs
    return temp

print(twitter(user_input))

```
# plates
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



main()


```
# nutrition
```
fruit_nutrition = {
    "apple":"130",
    "avocado":"50",
    "banana":"110",
    "cantaloupe":"50",
    "grapefruit":"60",
    "grapes": "90",
    "honeydew": "50",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
    "nectarine":"60",
    "orange":"80",
    "peach":"60",
    "pear": "100",
    "pineapple":"50",
    "plums":"70",
    "strawberries":"50",
    "sweet cherries":"100",
    "tangerine":"50",
    "watermelon":"80"
}

user_input = input("Item: ").lower().strip()

if user_input in fruit_nutrition:
    print("Calories: "+fruit_nutrition[user_input])

```
