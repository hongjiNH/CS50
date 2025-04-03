user_input = input("Expression: ").strip().split(" ")
x,y,z = user_input
x = float(x)
z = float(z)
match y:
        case "+":
              print(x+z)
        case "-":
              print(x-z)
        case "*":
             print(x*z)
        case "/":
            print(round(x/z,1))

