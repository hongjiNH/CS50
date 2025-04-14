menu={
    0:"Welcome to Smart Budget Buddy!",
    1:"Add a transaction",
    2:"View summary",
    3:"View spending by category",
    4:"Exit"
}

transactions = [
    {"amount":50,"category":"food","type":"expense"},
    {"amount":10,"category":"food","type":"expense"},
    {"amount":100,"category":"gift","type":"income"}
    ]

def main():
    while True:
        display_menu()
        try:
            user_choice = int(input("\n>> Choose an option: "))
        except ValueError:
            print("❌ Invalid choice! Please enter a number from 1 to 4.")
            continue

        match user_choice:
            case 1:
                while True:
                    try:
                        amount = float(input("Enter the amount: "))
                        break
                    except ValueError:
                        print("❌ Invalid amount! Please enter a valid number.")

                while True:
                    category = input("Enter the category: ").strip().lower()
                    if category:
                        break
                    else:
                        print("❌ Category cannot be empty.")

                while True:
                    types = input("Enter the type ('income' or 'expense'): ").strip().lower()
                    if types in ["income", "expense"]:
                        break
                    else:
                        print("❌ Type must be either 'income' or 'expense'.")

                add_transaction(amount, category, types)
                continue
            case 2:
                get_summary()
                continue
            case 3:
                category =input("Enter the category: ").lower()
                category_spending(category)
                continue
            case 4:
                print("Thank for using")
                break
            case _:
                print("❌ Invalid option! Please choose a number from 1 to 4.")

def add_transaction(amount, category, types):
    new_entry  = {
        "amount":amount,
        "category":category.lower(),
        "type":types.lower()
        }
    transactions.append(new_entry)
    print("✅ Transaction added successfully.")

def get_summary():
    filtered = [item for item in transactions]
    for item in filtered:
        print(f" {item['type'].title()}: ${item['amount']} | Category: {item['category'].title()}")

def category_spending(category):
    filtered = [item for item in transactions if item["category"].lower() == category.lower()]

    if not filtered:
        print(f"❌ No transactions found for category '{category}'.")
        return

    print(f"📂 Transactions for category '{category}':")
    for item in filtered:
        print(f"{item['type'].title()}: ${item['amount']}")

def display_menu():
    print("\n" + menu[0])
    for key in sorted(menu.keys()):
        if key != 0:
            print(f"{key}. {menu[key]}")

if __name__ == "__main__":
    main()
