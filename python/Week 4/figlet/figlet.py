import pyfiglet
import sys

try:
    if len(sys.argv)==3 and (sys.argv[1] =="-f" or sys.argv[1] =="--font"):
        pyfiglet.figlet_format("test",font=sys.argv[2])
        user_input = input("Input: ").strip()
        print(f"Output:\n {pyfiglet.figlet_format(user_input,font=sys.argv[2])}")
    else:
        if len(sys.argv)==1:
            user_input = input("Input: ").strip()
            print(f"Output:\n {pyfiglet.figlet_format(user_input)}")
        else:
            sys.exit("Invalid usage")

except:
    sys.exit("Invalid usage")




