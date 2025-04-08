import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'^.*iframe src=\"(?:https?://)?(?:www\.)?youtube\.com/(?:embed/)?([a-zA-Z0-9_-]{11})\".*$', s, re.IGNORECASE)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
