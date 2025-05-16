import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., food, transport, etc.): ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])
    print("Expense added successfully.\n")

def view_expenses():
    print("\nYour Expenses:")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Amount: ₹{row[0]} | Category: {row[1]} | Date: {row[2]}")
    print()

def main():
    print("=== Personal Expense Tracker ===")
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    # Initialize file with headers if it doesn't exist
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date"])
    except FileExistsError:
        pass

    main()
