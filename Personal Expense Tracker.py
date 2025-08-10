import csv
from datetime import datetime

class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def to_list(self):
        return [self.date, self.category, str(self.amount), self.description]

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from CSV file"""
        try:
            with open(self.filename, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # skip header
                for row in reader:
                    date, category, amount, description = row
                    self.expenses.append(Expense(date, category, float(amount), description))
        except FileNotFoundError:
            with open(self.filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Amount", "Description"])

    def add_expense(self, category, amount, description):
        """Add a new expense"""
        date = datetime.now().strftime("%Y-%m-%d")
        expense = Expense(date, category, amount, description)
        self.expenses.append(expense)
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(expense.to_list())
        print("✅ Expense added successfully!")

    def view_expenses(self):
        """Display all expenses"""
        print("\n📜 All Expenses:")
        for exp in self.expenses:
            print(f"{exp.date} | {exp.category} | ₹{exp.amount} | {exp.description}")

    def total_by_category(self, category):
        """Calculate total expense in a category"""
        total = sum(exp.amount for exp in self.expenses if exp.category.lower() == category.lower())
        print(f"\n💰 Total in '{category}': ₹{total}")

    def total_expense(self):
        """Calculate total expense"""
        total = sum(exp.amount for exp in self.expenses)
        print(f"\n💰 Total Expenses: ₹{total}")

# =======================
# Main Program
# =======================
tracker = ExpenseTracker()

while True:
    print("\n===== Expense Tracker Menu =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total by Category")
    print("4. Total Expenses")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        tracker.add_expense(category, amount, description)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        category = input("Enter category to check total: ")
        tracker.total_by_category(category)

    elif choice == "4":
        tracker.total_expense()

    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
