# Day 4 Practice Assignments: Dictionaries & Exception Handling
# Easy Assignments
# Assignment 1: Inventory Tracker for CDAC Bookstore
inventory = {"Python Basics": 10, "Learning AI": 5}


def manage_bookstore_inventory(inventory, action, book_title, quantity=0):

    if action.lower() == "add":
        if book_title in inventory:
            inventory[book_title] += quantity

        else:
            inventory[book_title] = quantity

    elif action.lower() == "sell":
        if book_title in inventory:
            if inventory[book_title] - quantity < 0:
                print(
                    f"Insufficient stock for '{book_title}'. Available: {inventory[book_title]}."
                )
            elif inventory[book_title] - quantity == 0:
                inventory.pop(book_title)
            else:
                inventory[book_title] -= quantity
        else:
            print(f"Book '{book_title}' not found in inventory.")

    elif action.lower() == "lookup":
        ...
    print(inventory)


# while True:
#     action = input(f"Enter the action what you want to do (add, sell, lookup, exit ): ")
#     input
#     if action.lower() in ["add", "sell", "lookup"]:
#         if action.lower == "lookup":
#             print(inventory)
#         else:
#             book_title = input("Enter the book titel: ")
#             quantity = int(input("Enter the numner of quantity: "))
#             manage_bookstore_inventory(inventory, action, book_title, quantity)
#     else:
#         break


# Assignment : Atomic E-Commerce Order Processor