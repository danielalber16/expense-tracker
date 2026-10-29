expenses = []

while True:
    print("1. Add expense")
    print("2. See expenses")
    print("3. Total expenses")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        description = input("Description: ")
        category = input("Category: ")
        amount = float(input("Amount: $"))
        expense = {"description": description, "category": category, "amount": amount}
        expenses.append(expense)
        print("Expense added!")
    elif option == "2":
        for expense in expenses:
            print(f"{expense['description']} - {expense['category']} - ${expense['amount']:.2f}")
    elif option == "3":
        total = 0
        for expense in expenses:
            total += expense['amount']
        print(f"Total: ${total:.2f}")
    elif option == "4":
        print("Goodbye!.")
        break
    else:
        print("Invalid Option")
