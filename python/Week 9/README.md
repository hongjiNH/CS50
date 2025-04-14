# Design Document

By hongjiNH

Video overview: <https://youtu.be/8AQpwJtvyPY>

# 💸 Smart Budget Buddy

Python app to help you track your income and expenses.
Organize your transactions by category, calculate your remaining balance, and stay on top of your budget

---

## 📌 Features

- Add income and expenses with categories
- Get a summary of total income, expenses, and balance
- Track how much you've spent in each category
- Prevent overspending with helpful summaries
- Easy-to-run tests with `pytest`

---

## 🗂️ Project Structure
/project-folder  
│  
│── project.py          # contains main and 3+ required functions  
└── test_project.py     # contains pytest functions for testing

---

# Install this before testing
```
pip install -r requirements.txt
```
# Run the app
```
python project.py

```
# Run tests(requires pytest)
```
pytest test_project.py
```
# Info for pytest
As im not using return for my functions  
So im using `capfd.readouterr()`
Using this to capture stdout/stderr output  
https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-capfd  
`out:` contains everything printed to the console (stdout)  
 `_:` contains everything printed to stderr (which we’re ignoring here with _)  

---

# Functios Overview
```
main()
```
- CLI for adding transactions and viewing summaries

```
add_transaction(amount, category, type)
```
- Adds an income or expense record

```
get_summary()
```
- Returns total income, total expenses, and balance

```
category_spending(category)
```
- Returns total amount spent in a specific category
