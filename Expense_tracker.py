#Expense Tracker Project

expenses = [] #list of all expenses

while True:
    print("===MENU===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Kharcha")
    print("4. Exit")

    choice=int(input("Enter your choices:"))
    if(choice==1):
        date=input("Enter the date of the expense (dd/mm/yyyy): ")
        category=input("Enter the category of the expense (eg: food, transport,books,etc..): ")
        description=input("Enter the description of the expense: ")
        amount=float(input("Enter the amount spent: "))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("Expense added successfully !\n")

        