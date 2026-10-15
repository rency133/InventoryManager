INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Displays all menu options for user to choose from"""
    
    print("Please enter an option from the following list: \n")
    print("\t--Inventory Manager--\n")
    print("1. View current inventory")
    print("2. Add item")
    print("3. Update item quantity")
    print("4. Remove item")
    print("5. Search current inventory")
    print("6. View inventory summary")
    print("7. Exit")

def load_inventory(filename):
    pass

def save_inventory(inventory, filename):
    pass

def view_inventory(inventory):
    pass

def add_item(inventory):
    pass

def update_quantity(inventory):
    pass

def remove_item(inventory):
    pass

def search_inventory(inventory):
    pass

def display_summary(inventory):
    pass

def main():
    # loop display menu until user chooses exit option
    while True:
        display_menu()
        option = input("\nYour choice: ") # get user input

        match option: # match user option
            case "1":
                print("view inventory")
            case "2":
                print("add item")
            case "3":
                print("update item")
            case "4":
                print("remove item")
            case "5": 
                print("search inventory")
            case "6":
                print("view inventory summary")
            case "7":
                print("exit")
                break
            case _:
                print("*" * 20)
                print("Error: \tOnly 1-7 are valid options")
                print(("*" * 20) + "\n")

if __name__=="__main__":
    main()