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
