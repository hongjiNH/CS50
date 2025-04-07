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
