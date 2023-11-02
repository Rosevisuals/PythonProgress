
inventory = []

def add_item(item_name, quantity):
    for i, (name, stock) in enumerate(inventory):
        if name == item_name:
            inventory[i] = (name, stock + quantity)
            break
    else:
        inventory.append((item_name, quantity))

def remove_item(item_name, quantity):
    for i, (name, stock) in enumerate(inventory):
        if name == item_name:
            if quantity < stock:
                inventory[i] = (name, stock - quantity)
            else:
                inventory.pop(i)
            break

def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for name, stock in inventory:
            print(f"{name}: {stock}")

while True:
    print("Options:")
    print("1. Add items")
    print("2. Remove items")
    print("3. View inventory")
    print("4. Exit program")

    option = input("Enter choice (1/2/3/4): ")

    if option == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_item(item_name, quantity)
        print(f"{item_name} {quantity} added to inventory.")
    elif option == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        remove_item(item_name, quantity)
    elif option == '3':
        view_inventory()
    elif option == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid option, enter a valid option")
