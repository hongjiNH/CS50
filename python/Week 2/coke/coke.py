amount = 50

while amount >0:
    print("Amount Due:",amount)
    user_input = int(input("Insert Coin: "))

    if user_input ==25 or user_input == 10 or user_input ==5:
        amount -= user_input
        continue

if amount < 0:
    print("Change Owed:", amount*-1)
else:
    print("Change Owed:", amount)


