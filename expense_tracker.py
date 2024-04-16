class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})

    def total_expenses(self):
        total = sum(item['amount'] for item in self.expenses)
        return total

    def category_expenses(self, category):
        total = sum(item['amount'] for item in self.expenses if item['category'] == category)
        return total

    def show_expenses(self):
        for item in self.expenses:
            print(f"Category: {item['category']}, Amount: ${item['amount']}")

# Main program
tracker = ExpenseTracker()

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Show Total Expenses")
    print("3. Show Expenses by Category")
    print("4. Show All Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        tracker.add_expense(category, amount)
        print("Expense added successfully!")
    elif choice == '2':
        print(f"Total Expenses: ${tracker.total_expenses()}")
    elif choice == '3':
        category = input("Enter the category: ")
        print(f"Total Expenses for {category}: ${tracker.category_expenses(category)}")
    elif choice == '4':
        print("All Expenses:")
        tracker.show_expenses()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
