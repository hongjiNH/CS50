#  fuel
```
while True:
    try:
        user_input = input("Fraction: ").split("/")
        x,y = user_input
        x = int(x)
        y = int(y)
        percentage = round((x/y)*100)
        if percentage <= 1:
            print("E")
            break
        elif percentage>=99:
            if percentage >100:
                continue
            else:
                print("F")
                break
        else:
            print(str(percentage)+"%")
            break
    except (ValueError, ZeroDivisionError):
        pass

```
# taqueria
```
food = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        item = input("Item: ").title()
        if item in food:
            total +=food[item]
            print(f"Total: ${total:.2f}")
    except (EOFError):
        print("item: ")
        break


```
# grocery
```

user_List={}
while True:
    try:
        item = input().upper()

        if item  in user_List:
            user_List[item] += 1
        else:
            user_List[item] = 1

    except EOFError:

        for item, count in dict(sorted(user_List.items())).items():
            print(count, item)
        break


```
# outdated
```
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

year = 0
month = 0
day = 0

while True:
    try:
        user_input = input("Date: ").title()

        if "/" in user_input:
            temp = user_input.split("/")
            if int(temp[0]) <=12 and int(temp[1]) <=31:
                day = temp[1]
                month = temp[0]
                year = temp[2]

                if int(temp[0]) < 10:
                    month = "0"+temp[0]

                if int(temp[1]) <10:
                    day ="0"+temp[1]

                print(f"{year.replace(" ","")}-{month.replace(" ","")}-{day}")
                break

        if " " in user_input:
            if user_input.find(",") != -1:
                temp = user_input.replace(",","")
                temp = temp.split(" ")
                if int(temp[1]) <=31:
                    day = temp[1]

                    year = temp[2]

                    if temp[0] in months:
                        if months.index(temp[0])+1 < 10:
                            month = "0"+str(months.index(temp[0])+1)
                        else:
                            month = months.index(temp[0])+1

                    if int(temp[1]) <10:
                        day ="0"+temp[1]

                    print(f"{year}-{month}-{day}")
                    break

            continue

    except ValueError:
        pass
```
