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
        json.dump(expenses,file)

def load_expenses():
    with open(FILE_PATH, "r") as file:
        return json.load(file)
        

expenses = load_expenses()


while True:
    print("*****************")
    print("EXPENSE TRACKER")
    print("*****************")

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total Spending")
    print("4. Delete Expense")
    print("5. EXIT")

    choice = input("Enter your choice (1-5): ")

    match choice:
        case "1":
            category =  input("Enter category of expense: ")
            item_name = input("Enter item name: ")
            price = float(input(f"Enter {item_name}'s price: "))

            expense = {
                "category" :category,
                "item_name" : item_name,
                "price": price
            }

            expenses.append(expense)
            save_expenses()

            print("Expense added successfully")
            pause()


        case "2":
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

         
        case "3":
            total =0
            if not expenses :
                print("No Expenses Found")
                pause()

            else:
                for expense in expenses :
                    total+= expense["price"]

                print("-" * 50 )    
                print(f"Total Spending : ₹{total}")    
                print("-" * 50 )
                
                pause()    
       
        case "4":
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
           
                delete_exp = int(input("\nEnter expense to be deleted : "))

                if 1<=delete_exp <= len(expenses):
                    deleted_expense= expenses.pop(delete_exp-1)
                    print(f"{deleted_expense['item_name']} Deleted Successfully")
                    pause()
                else :
                    print("Invalid expense number")
                    pause()

        case "5":
            print("EXITING NOW !")
            break      
        
        case _:
            print("Invalid Choice")
            pause()




