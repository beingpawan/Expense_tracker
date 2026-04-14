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

        #2. View Expenses
    elif(choice==2):
        if(len(expenses)==0):
            print("No expenses to show !\n")
        else:
                print("===Expenses List===")
                count=1
                for eachexpense in expenses:
                   print(f"Expense number: {count} -> Date: {eachexpense["date"]}, Category: {eachexpense["category"]}, Description: {eachexpense["description"]}, Amount: {eachexpense["amount"]}")
                   count=count+1

      
         