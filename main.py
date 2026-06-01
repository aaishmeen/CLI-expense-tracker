import json
import os
FILE_PATH = os.path.join(os.path.dirname(__file__), "expenses.json")


def clear_screen():
    os.system("cls")


def pause():
    input('\nPress Enter to continue....')
    clear_screen() 


def save_expenses():
    
    with open(FILE_PATH, "w") as file:
        json.dump(expenses,file,indent=4)


def load_expenses():

    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r") as file:
        return json.load(file)


def add_expense():
    category =  input("Enter category of expense: ")
    item_name = input("Enter item name: ")

    try:
         price = float(input(f"Enter {item_name}'s price: "))

    except ValueError:
        print("Please Enter a Valid Price ")  
        pause()
        return   

    expense = {
        "category" :category,
        "item_name" : item_name,
        "price": price
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully")
    pause()



def view_expenses():
     if not expenses :
        print("No Expenses Found")
        pause() 

     else:
        print('-' *50)
        print(f"{'Category':<15} {'Item':<20} {'Price':<10}")
        print("-" * 50)

        for expense in expenses:
            print(f"{expense['category']:<15} {expense['item_name']:<20} ₹{expense['price']:<10}")
        
        print("-" * 50)
        pause() 



def show_total_spending():
     
     total =0

     if not expenses :
        print("No Expenses Found")
        pause()

     else:

        for expense in expenses :
             total+= expense["price"]

        print("-" * 50 )   
        print(f"Total Expenses: {len(expenses)}") 
        print(f"Total Spending : ₹{total:.2f}")    
        print("-" * 50 )
        
        pause()



def delete_expense():
    if not expenses :
        print("No Expenses Found")
        pause()

    else:  

        print("-" * 65)
        print(f"{'No.':<5} {'Category':<15} {'Item':<20} {'Price':<10}")
        print("-" * 65)

        for index, expense in enumerate(expenses, start=1):
            print(
                f"{index:<5} "
                f"{expense['category']:<15} "
                f"{expense['item_name']:<20} "
                f"₹{expense['price']:<10}"
            )
        print("-" * 65) 

        try: 
           delete_exp = int(input("\nEnter expense to be deleted : "))
        except ValueError :
            print("Please Enter a Valid Number: ")
            pause()
            return 
        
        if 1<=delete_exp <= len(expenses):
            deleted_expense= expenses.pop(delete_exp-1)
            save_expenses()
            print(f"{deleted_expense['item_name']} Deleted Successfully")
            pause()
        else :
            print("Invalid expense number")
            pause()

def search_expenses():

    if not expenses:
        print("No Expenses found")
        pause()
        return
    
    search= input("Enter category to search: ")

    matched_expenses = []
    
    for expense in expenses:
        if search.lower() in expense["category"].lower():
           matched_expenses.append(expense)

    if not matched_expenses:
        print("No matching expenses found.")
        pause()

    else :
        print("-" * 50)
        print(f"{'Category':<15} {'Item':<20} {'Price':<10}")
        print("-" * 50)

        for expense in matched_expenses:
            print(
                f"{expense['category']:<15} "
                f"{expense['item_name']:<20} "
                f"₹{expense['price']:<10}"
            )

        print("-" * 50)

        pause()



expenses = load_expenses()


while True:
    print("*****************")
    print("EXPENSE TRACKER")
    print("*****************")

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total Spending")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. EXIT")

    choice = input("Enter your choice (1-6): ")

    match choice:
        case "1":
            add_expense()
           
        case "2":
            view_expenses()
           
        case "3":
            show_total_spending()
               
        case "4":
            delete_expense()

        case "5":
            search_expenses()    
           
        case "6":
            print("EXITING NOW !")
            break      
        
        case _:
            print("Invalid Choice")
            pause()




