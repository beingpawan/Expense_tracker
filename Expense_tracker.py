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
                   print(f"Expense number: {count} -> {eachexpense["date"]}, Category: {eachexpense["category"]} -> {eachexpense["description"]}, Amount: {eachexpense["amount"]}")
                   count=count+1

        #3. View Total Expenses
    elif(choice==3):
         total = 0
         for eachexpense in expenses:
                 total += eachexpense["amount"]
         print("\nTotal Expenses:  ",total)
         print("\n")
 
        #4. EXIT
    elif(choice==4):
        print("Thank you for using the Expense Tracker App. Goodbye! ")
        break
    else:
        print("Invalid choice. PLease try again !\n")

         