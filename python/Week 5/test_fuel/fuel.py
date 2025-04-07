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
