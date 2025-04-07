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
