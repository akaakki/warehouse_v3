"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from data import stock
from get_personnel_data import log_user_in

operation_history = []

def get_user_name():

    user_name = input("Hello! What is you name: ")
    return user_name

def greet_user(user_name):

    print(f"Hello, {user_name}")
    

def get_selected_operation():
    print("(1) List items by warehouse (2) Search an item an place an order (3) Quit")
    return input("Which option do you choose: ")

def show_user_menu():
    
    operation = get_selected_operation()

    if operation == "1":
        list_items_by_warehouse()
    elif operation == "2":
        search_item()
    elif operation == "3":
        browse_by_category()
    elif operation == "4":
        pass
    else:
        error_message()

def list_items_by_warehouse():
    
    for a in range(1,5):
        print(f"All the items in Warehouse {a}")
        for item in stock:
            if item['warehouse'] == a:
                print(item['category'])

    operation_history.append("You listed all 5000 items.")

    user_choice_restart_operation = input("Do you want to start over (y/n): ")
        
    if user_choice_restart_operation == 'y':
        show_user_menu()


def search_item():

    item_searched = input("What item do you want to search: ")
    return print_result(item_searched)

def print_result(item_searched):

    count_searched_item = 0
    for item in stock:
        if item['category'] == item_searched:
            count_searched_item += 1
    print(f'Amount of items in all the Warehouses: {count_searched_item}')
    overall_amount_item = count_searched_item

    location_amount = {}
    count_searched_item = 0
    for a in range(1,5):
        for item in stock:
            if item['warehouse'] == a:
                if item['category'] == item_searched:
                    current_warehouse = "Warehouse " + str(item['warehouse'])
                    count_searched_item += 1
                    if not current_warehouse in location_amount:
                        location_amount[current_warehouse] = 1
                    else:
                        location_amount[current_warehouse] += 1

    if location_amount != None:
        for key, value in location_amount.items():
            print(f"{key}: {value}")   
    else:
        print("Item is not in stock.") 

    max_amount_item_location = max(location_amount, key=location_amount.get)
    max_amount_item = max(location_amount.values())
    print(f"The hightest amount of that item you can find in {max_amount_item_location}. It has {max_amount_item} item(s).")

    user_place_order = input("You want to place an order for this item (y/n): ")

    if user_place_order == "y":
        return order_item(item_searched, location_amount, overall_amount_item)
    else:
        user_choice_restart_operation = input("Do you want to start over (y/n): ")
                
        if user_choice_restart_operation == 'y':
        
            operation = get_selected_operation()
            if operation == "1":
                list_items_by_warehouse()
            elif operation == "2":
                search_and_order_item()
            elif operation == "3":
                browse_by_category()
            elif operation == "4":
                pass
            else:
                error_message()
        

def check_login(func):
    def wrapper(*args):
        continue_auth = True
        while continue_auth:
            global user_logged_in
            global user_name
            if user_logged_in:
                return func(*args)
            
            user_logged_in = log_user_in(user_name)
            if not user_logged_in:
                user_name = None
                user_input = input("You wanna continue to log in (y/n): ")
                continue_auth = True if user_input == "y" else False

    return wrapper

@check_login
def order_item(item_searched, location_amount, overall_amount):

    user_item_ordered_amount = int(input("Which amount of the item do you want to order: "))
    if user_item_ordered_amount <= overall_amount:
        print(f"The order has been placed. You have ordered {item_searched}: {user_item_ordered_amount} time(s)")
    elif user_item_ordered_amount > overall_amount:
        print("You exceeded the maxmium amount.")
        user_item_order_max_amount = input("Do you want to order the maximum amount of the item (y/n): ")
        if user_item_order_max_amount == "y":
            print("Order has been placed.")
            print(f"You order {item_searched}. You ordered it {overall_amount}.")
        elif user_item_order_max_amount == "n":
            pass
        else:
            print("Invalid input Please start over again.")

    operation_history.append(f"You searched {item_searched}.")

    user_choice_restart_operation = input("Do you want to start over (y/n): ")
        
    if user_choice_restart_operation == 'y':
        show_user_menu()

def browse_by_category():

    pass

def error_message():

    print("*" * 50)
    print("You didnt enter a valid operation.")
    print("*" * 50)
    
    get_selected_operation()

### Get the user name and greet
user_name = get_user_name()
user_logged_in = False

greet_user(user_name)

### Get the user selection

show_user_menu()

### Finish
print(f"Thank you for your visit, {user_name}")
counter = 0
print("In this session you have:")
for operation in operation_history:
    counter += 1
    print(f"{counter}. {operation}")