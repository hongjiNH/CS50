from project import add_transaction, transactions, category_spending, get_summary

def test_add_transaction():
    add_transaction(25, "entertainment", "expense")
    assert transactions[-1] == {"amount": 25, "category": "entertainment", "type": "expense"}

def test_category_spending_found(capfd):
    category_spending("food")
    out, _ = capfd.readouterr()
    assert "📂 Transactions for category 'food'" in out
    assert "Expense: $50" in out
    assert "Expense: $10" in out

def test_category_spending_not_found(capfd):
    category_spending("travel")
    out, _ = capfd.readouterr()
    assert "No transactions found for category 'travel'" in out

def test_get_summary(capfd):
    get_summary()
    out, _ = capfd.readouterr()
    assert " Expense: $50 | Category: Food" in out
    assert " Expense: $10 | Category: Food" in out
    assert " Income: $100 | Category: Gift" in out
    assert " Expense: $25 | Category: Entertainment" in out
