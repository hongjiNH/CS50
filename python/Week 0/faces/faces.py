def main():
    user_input=input()
    print(convert(user_input))

def convert(user_input):

    temp =  user_input.replace(":)","🙂")
    return temp.replace(":(","🙁")

main()


