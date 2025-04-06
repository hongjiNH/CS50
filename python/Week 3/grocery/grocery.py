
user_List={}
while True:
    try:
        item = input().upper()

        if item  in user_List:
            user_List[item] += 1
        else:
            user_List[item] = 1

    except EOFError:

        for item, count in dict(sorted(user_List.items())).items():
            print(count, item)
        break
