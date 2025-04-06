user_input = input("camelCase: ")

def camel(user_input):
    temp = ""
    for inputs in user_input:
        if inputs.isupper():
            temp += "_" + inputs.lower()
        else:
            temp += inputs

    return temp

print(camel(user_input))
