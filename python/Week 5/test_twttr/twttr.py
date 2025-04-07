def main():
    user_input = input("Input: ").strip()
    print(shorten(user_input))


def shorten(word):
    temp =""
    for inputs in word:
        if inputs.lower() == "a" or inputs.lower() == "e" or inputs.lower() == "i" or inputs.lower() == "o" or inputs.lower() == "u":
            temp = temp
        else:
            temp += inputs
    return temp


if __name__ == "__main__":
    main()
