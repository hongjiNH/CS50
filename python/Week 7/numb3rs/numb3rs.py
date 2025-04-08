from re import search

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    temp = "(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    if search("^" + r"\.".join([temp] * 4) + "$",ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
