def main():
    time = input("What time is it? ").strip()
    hours = convert(time)

    if 7 <= hours <= 8:
        print("Breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + (int(minutes) / 60) 

if __name__ == "__main__":
    main()
