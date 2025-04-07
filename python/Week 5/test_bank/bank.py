def main():
    user_input = input("Greeting: ").lower().strip()
    print(f"${value(user_input)}")

def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
