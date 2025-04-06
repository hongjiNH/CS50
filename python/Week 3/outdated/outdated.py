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
