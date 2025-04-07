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
