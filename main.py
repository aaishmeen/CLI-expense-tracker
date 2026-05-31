expenses =[]

while True:
    print("*****************")
    print("EXPENSE TRACKER")
    print("*****************")

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    match choice:
        case "1":
            category =  input("Enter category of expense: ")
            item_name = input("Enter item name: ")
            price = input(f"Enter {item_name}'s price: ")

            expense = {
                "category" :category,
                "item_name" : item_name,
                "price": price
            }

            expenses.append(expense)

            print("Expense added successfully")


        case "2":
            print('-' *50)
            print(f"{'Category':<15} {'Item':<20} {'Price':<10}")
            print("-" * 50)

            for expense in expenses:
                print(f"{expense['category']:<15} {expense['item_name']:<20} ₹{expense['price']:<10}")
               
            print("-" * 50)    



        case "3":
            print("EXITING NOW !")
            break      
        
        case _:
            print("Invalid Choice")




