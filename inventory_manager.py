INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Displays all menu options for user to choose from"""
    
    print("\nPlease enter an option from the following list: \n")
    print("\t--Inventory Manager--\n")
    print("1. View current inventory")
    print("2. Add item")
    print("3. Update item quantity")
    print("4. Remove item")
    print("5. Search current inventory")
    print("6. View inventory summary")
    print("7. Exit")

def load_inventory(filename):
    """Open and read file and create a list of dictionaries storing each items' name, category, and quantity"""
    items = [] # list of dictionaries
    key_names = ["name", "category", "quantity"] # list of cateogory names
    
    try: # try except block for opening and reading file
        with open(filename, "r") as file:
            for line in file: 
                keys = line.strip().split("|")
                i = 0
                item = {} # create dictionary
                for key in keys:
                    if i == 2: # key_names[2] = quantity and should be converted to int
                        key = int(key)
                    item[key_names[i]] = key
                    i += 1 # next item in key_items
                items.append(item) # add each dictionary to a list

    except FileNotFoundError:
        # if inventory.txt doesn't exist, return empty list
        return []

    return items # return list of dictionaries

def save_inventory(inventory, filename):
    """Save all changes to a text file."""
    new_item = ""
    with open(filename, "w") as file:
        for item in inventory:
            file.write(f"{item.get("name")}|{item.get("category")}|{item.get("quantity")}\n")
    
def view_inventory(inventory):
    if not inventory:
        print("No inventory items found.")
        return

    print("\n\t--Current Inventory List--\n")
    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item.get('name')} | {item.get('category')} | Quantity: {item.get('quantity')}")

def add_item(inventory):
    i = 0
    name = ""
    category = ""
    quantity = ""
    new_item = {}

    while i < 4:
        match i:
            case 0:
                name = input("Enter item name: ")
                if not name: 
                    print("Please enter item name")
                elif name.__contains__("|"):
                    print("Item name cannot contain '|'")
                else:
                    new_item["name"] = name.casefold()
                    i = 1
            case 1:
                category = input("Enter item category: ")
                if not category:
                    print("Please enter item category")
                elif category.__contains__("|"):
                    print("Item category cannot contain '|'")
                else:
                    new_item["category"] = category
                    i = 2
            case 2:
                quantity = input("Enter item quantity: ")
                if not quantity:
                    print("Please enter item quantity")
                else:
                    i = 3
            case 3:
                try:
                    quantity = int(quantity)
                    if quantity < 0:
                        print("Please enter a positive quantity")
                    else:
                        new_item["quantity"] = quantity
                        i = 4
                        break
                        
                except TypeError:
                    print("Please enter a number")
                except ValueError:
                    print("Please enter an integer")
                finally:
                    i = 2
            case _:
                i = 5
    for item in inventory:
        item_name = item.get("name")
        if item_name.casefold() == name:
            print("Item already exists in inventory")
            return

    inventory.append(new_item)
    print(f"{name} successfully added to inventory.")

def update_quantity(inventory):
    if not inventory:
        print("No inventory items found.")
        return
    
    print("\nPlease enter the number of the item you wish to update from the following list: \n")
    view_inventory(inventory)
    choice = input("Your choice: ")
    try:
        choice = int(choice)
        if choice < 0 or choice > len(inventory):
            raise ValueError("Please enter a number associated with an item.")
    except TypeError:
        print("Please enter a number.")
        return
    except ValueError as e:
        print(e)
        return

    item = inventory[choice - 1]
    print(f"\nItem chosen: {item.get("name")}\nCurrent Quantity: {item.get("quantity")}\n")
    new_quantity = input("Please enter the updated quantity: ")
    try:
        new_quantity = int(new_quantity)
        if new_quantity < 0:
            print("Please enter a positive quantity")
        else:
            item["quantity"] = new_quantity
                
    except TypeError:
            print("Please enter a number")
            return
    except ValueError:
        print("Please enter an integer")
        return

    print(f"{item.get("name")} updated quantity to {item.get("quantity")}")

def remove_item(inventory):
    if not inventory:
        print("No inventory items found.")
        return
    
    print("\nPlease enter the number of the item you wish to remove from the following list: \n")
    view_inventory(inventory)
    choice = input("Your choice: ")
    try:
        choice = int(choice)
        if choice < 0 or choice > len(inventory):
            raise ValueError("Please enter a number associated with an item.")
    except TypeError:
        print("Please enter a number.")
        return
    except ValueError as e:
        print(e)
        return

    removed_item = inventory.pop(choice - 1)
    print(f"\nRemoved {removed_item.get("name")} from inventory.")

def search_inventory(inventory):
    pass

def display_summary(inventory):
    pass

def main():
    inventory = load_inventory(INVENTORY_FILE) # load inventory.txt
    # loop display menu until user chooses exit option
    while True:
        display_menu()
        option = input("\nYour choice: ") # get user input

        match option: # match user option
            case "1":
                view_inventory(inventory)
            case "2":
                add_item(inventory)
                save_inventory(inventory, INVENTORY_FILE)
            case "3":
                update_quantity(inventory)
                save_inventory(inventory, INVENTORY_FILE)
            case "4":
                remove_item(inventory)
                save_inventory(inventory, INVENTORY_FILE)
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