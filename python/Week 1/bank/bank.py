user_input = input("Greeting: ").lower().strip()
if "hello" in user_input:
    print("$0")
elif user_input.startswith("h"):
    print("$20")
else:
    print("$100")
