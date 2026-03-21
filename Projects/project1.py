# Personal Finance Manager (File Handling + Error Handling + Data Processing)

import csv
from datetime import datetime

FILE_NAME = "expenses.csv"
LOG_FILE = "error_log.txt"


def log_error(error):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} : {error}\n")

def add_expenses():
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter Amount: "))
        note = input("Enter note: ")
        
        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, note])

        print("Expenses saved succesfully!")

    except:
        print("Invalid amount entered")
        log_error("Invalid amount input")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n ------- Epenses List --------")

            for row in reader:
                print(row)

    except:
        print("Expense file not found")
        log_error("Expense file not found while viewing expeses")


def search_category():
    try:
        category = input("Enter category to search: ")
        found = False

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[1].lower() == category.lower():
                    print(row)
                    found = True

        if not found:
            print("No records found")

    except Exception as e:
        print("Error while searching...")
        log_error(e)


def delete_expense():
    try:
        date = input("Enter date of expense to delete: ")

        rows = []
        deleted = False

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0] != date:
                    rows.append(row)
                else:
                    deleted = True

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        if deleted:
            print("Expense deleted")
        else:
            print("Expense not found")

    except Exception as e:
        print("Error dealing expense")
        log_error(e)


def monthly_expense():
    try:
        month = input("Enter month (YYYY-MM): ")
        total = 0

        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[0].startswith(month):
                    total += float(row[2])

        print("Total expense for month: ", total)

    except Exception as e:
        print("Error generating summary")
        log_error(e)


def menu():
    while True:
        print("\n ====== Finance Manager ======")
        print("1. Add Expense")
        print("2. View Epense")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Monthly Summary")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                add_expenses()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                search_category()

            elif choice == 4:
                delete_expense()
            
            elif choice == 5:
                monthly_expense()
            
            elif choice == 6:
                print("Thank you. Goodby!")
                break
            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter a valid number")
            log_error("menu input error")

menu()







            

