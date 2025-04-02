#indoor voice

user_input = input("hi you are: ")
print(user_input.lower())

#playback speed

user_input = input("Type our input here: ")
print(user_input.replace(" ","..."))

#making faces

def main():
    user_input=input()
    print(convert(user_input))

def convert(user_input):

    temp =  user_input.replace(":)","🙂")
    return temp.replace(":(","🙁")

main()

#einstein
user_input = int(input("m: "))
print("E: ",user_input*300000000 **2)

#tip calculator

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return(float(d.replace("$","")))


def percent_to_float(p):
    temp = int(p.replace("%",""))
    return(float(temp/100))


main()
