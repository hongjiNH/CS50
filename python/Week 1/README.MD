# Deep thought
```
user_input = input("What is the Answer to the Great Question of Life, the Universe and Everything").lower().strip()
if user_input == "42" or user_input== "forty-two" or user_input== "forty two":
    print("Yes")
else:
     print("no")

```
# Bank
```
user_input = input("Greeting: ").lower().strip()
if "hello" in user_input:
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")

```
# extension
```
user_input = input("File name: ").lower().strip()
if "gif" in user_input:
    print("image/gif")
elif "jpg" in user_input or "jpeg" in user_input:
    print("image/jpeg")
elif "png" in user_input:
    print("image/png")
elif "pdf" in user_input:
    print("application/pdf")
elif "txt" in user_input:
    print("text/plain")
elif "zip" in user_input:
    print("application/zip")
else:
    print("application/octet-stream")

```
# interpreter
```
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


```
# meal
```
def main():
    time = input("What time is it? ").strip()
    hours = convert(time)

    if 7 <= hours <= 8:
        print("Breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + (int(minutes) / 60) 

if __name__ == "__main__":
    main()

```
