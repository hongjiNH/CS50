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
