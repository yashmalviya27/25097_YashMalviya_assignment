import json
FILE_NAME = "inventory.json"
# Python Lab Examination
# ---------------------------------------------------------------------------------------+
#                              This is for the data store                                |
# ---------------------------------------------------------------------------------------+
products = [                                                                            #| 
{"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, #|
{"id": 2, "name": "Laptop", "category": "Furniture", "price": 1500, "quantity": 50}     #|
]                                                                                       #|
# ---------------------------------------------------------------------------------------+




# ---------------------------------------------------------------------------------------+
#                              this is for add the data                                  |
# ---------------------------------------------------------------------------------------+
def data_add():                                                                         #|
                                                                                        #|
    print("Add Product in Inventory")                                                   #|
    print("_" * 50)                                                                     #|
                                                                                        #|
    # ---------------- NAME ----------------                                            #|
    while True:                                                                         #|
        product_name = input("Enter the name of the product: ").strip().title()         #|
                                                                                        #|
        if not product_name:                                                            #|
            print("Product name cannot be empty.")                                      #|
                                                                                        #|
        elif not product_name.replace(" ", "").isalpha():                               #|
            print("Product name must contain only alphabets.")                          #|
                                                                                        #|
        else:                                                                           #|
            break                                                                       #|
                                                                                        #|
    # ---------------- CATEGORY ----------------                                        #|
    while True:                                                                         #|
        category = input("Enter the category of the product: ").strip().title()         #|
                                                                                        #|
        if not category:                                                                #|
            print("Category cannot be empty.")                                          #|
                                                                                        #|
        elif not category.replace(" ", "").isalpha():                                   #|
            print("Category must contain only alphabets.")                              #|
                                                                                        #|
        else:                                                                           #|
            break                                                                       #|
                                                                                        #|
    # ---------------- PRICE ----------------                                           #|
    while True:                                                                         #|
        product_price = input("Enter the price of the product: ").strip()               #|
                                                                                        #|
        try:                                                                            #|
            product_price = float(product_price)                                        #|
                                                                                        #|
            if product_price < 0:                                                       #|
                print("Price cannot be negative.")                                      #|
            else:                                                                       #|
                break                                                                   #|
                                                                                        #|
        except ValueError:                                                              #|
            print("Price must be a valid number.")                                      #|
                                                                                        #|
    # ---------------- QUANTITY ----------------                                        #|
    while True:                                                                         #|
        product_quantity = input("Enter the quantity of the product: ").strip()         #| 
                                                                                        #|
        try:                                                                            #|
            product_quantity = int(product_quantity)                                    #|
                                                                                        #|
            if product_quantity < 0:                                                    #|
                print("Quantity cannot be negative.")                                   #|
            else:                                                                       #|
                break                                                                   #|
                                                                                        #|
        except ValueError:                                                              #|
            print("Quantity must be a valid integer.")                                  #|
                                                                                        #|
    # ---------------- ID ----------------                                              #|
    if len(products) == 0:                                                              #|
        product_id = 1                                                                  #|
    else:                                                                               #|
        product_id = max(product["id"] for product in products) + 1                     #|
                                                                                        #|
    # ---------------- CREATE PRODUCT ----------------                                  #|
    inventory = {                                                                       #|
        "id": product_id,                                                               #|
        "name": product_name,                                                           #|
        "category": category,                                                           #|
        "price": product_price,                                                         #|
        "quantity": product_quantity                                                    #|
    }                                                                                   #|
    products.append(inventory)                                                          #|
    # ---------------- ADD TO LIST ----------------                                     #|
    print('----Product added successfully!----')                                        #|
    print(f"""   ID       : {inventory['id']}""")                                       #|
    print(f"""   Name     : {inventory['name']}""")                                     #|
    print(f"""   Category : {inventory['category']}""")                                 #|
    print(f"""   Price    : {inventory['price']}""")                                    #|
    print(f"""   Quantity : {inventory['quantity']}\n""")                               #|

    # ------------------- Display LIST ------------------
# =======================================================================================+


def data_dislpay():
    print("-"*60)
    print(f"{"ID":^5}{"Name":<20}{"Category":<10}{"print":>12}{"Quantity":>15}")
    print("-"*60)
    for product in products:
        id_, name, category, price, quantity = product.values()
        print(f"{id_:^5}{name:<20}{category:<10}{price:>12.2f}{quantity:>15}")
        print("-"*60)

    # ------------------- Search by id ------------------

def search_by_id():
    try:
        id_ = int(input("enter the id no:"))
    except Exception:
        print("this is is accor with unwanted choice.")
    for product in products:
        if product["id"] == id_:
            print("-"*50)
            print(f"           THIS IS YOR EXPECTED OURCOME")
            print("-"*50)
            print(f"""ID        : {product['id']}
Name      : {product['name']}
Category  : {product['category']}
Price     : {product['price']}
Quantity  : {product['quantity']}
""")
            print("-"*50)
            break
        else:
            print("No product found.")
        

    # ------------------ Search by name -----------------

def search_by_name():

    name = input("Enter the product name: ").strip().lower()

    for product in products:
        if product["name"].lower() == name:
            print(product)


    print("No product found.")

    # ----------------------- Search ----------------------

def search():
    text = """SELECT THE OPTION YOU WANT OT SEARCH WITH
1. ID_
2. NAME"""
    print(text)
    try:
        choice = int(input("Select the option: "))
    except ValueError:
            print(f"Wrong choice please try again")
            return
    
    match choice:
        case 1:
            search_by_id()
        case 2:
            search_by_name()
        case _:
            print(f"Wrong choice..!!")
# ------------------- update by id ------------------
def update_product():

    try:
        input_id = int(input("Enter the product ID: "))
    except ValueError:
        return "Invalid ID. Please enter a number."

    for product in products:

        if product["id"] == input_id:

            # Update name
            name = input(f"Enter new name [{product['name']}]: ").strip().title()

            if name:
                product["name"] = name

            # Update category
            category = input(f"Enter new category [{product['category']}]: ").strip().title()

            if category:
                product["category"] = category

            # Update price
            price = input(f"Enter new price [{product['price']}]: ").strip()

            if price:
                try:
                    price = float(price)

                    if price < 0:
                        print("Price cannot be negative.")
                    else:
                        product["price"] = price

                except ValueError:
                    print("Invalid price.")

            # Update quantity
            quantity = input(f"Enter new quantity [{product['quantity']}]: ").strip()

            if quantity:
                try:
                    quantity = int(quantity)

                    if quantity < 0:
                        print("Quantity cannot be negative.")
                    else:
                        product["quantity"] = quantity

                except ValueError:
                    print("Invalid quantity.")

            return "Product updated successfully."

    return "Invalid product ID."

def delet_item():
    try:
        id_ = int(input("Enter the id what you are deleting: "))
    except Exception:
        print("Invalide choice.")
    for product in products:
        if product["id"] == id_:
            print(f"""id        : {product['id']}
Name      : {product["name"]}
Category  : {product["category"]}
Price     : {product["price"]}
Quantity  : {product["quantity"]}""")
            result = input("Are you shour do you want to delet this user y/n: ").strip().title()
            if result=="Y":
                products.remove(product)
                print("Product delet succesfully.")
                break
            else:
                print("product id not deleted.")

def exprt_json():
        try:
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                json.dump(products, file, indent=4)
                print(f"Json export successful.")
        except Exception:
            print("somthing went wrong.")

# def load_json()

# --------------------------------------------------------+
#      This is the menu part which print the choice       |
# --------------------------------------------------------+
def menu():                                              #|
    print_01 = """1. Add products
2. View all products
3. Search products
4. Update products
5. Delete products
6. Exit from the system"""

    print("=" * 50)                                     #|
    print("       Product Inventory Management System") #|
    print("=" * 50)                                     #|
    print(print_01)                                     #|
    print("=" * 50)                                     #|
#                                                        |
    try:                                                #|
        choice = int(input("Enter your choice: "))      #|
        return choice                                   #|
    except ValueError:                                  #|
        return -1                                       #|
# -------------------------------------------------------+
#                                                        |
#                                                        |
# -------------------------------------------------------+


# ----------------------------------------------------+
# This is the entry point of the project              |
# ----------------------------------------------------+
def main():

    while True:

        choice = menu()

        match choice:

            case 1:
                data_add()

            case 2:
                data_dislpay()

            case 3:
                search()

            case 4:
                update_product()

            case 5:
                delet_item()

            case 6:
                print("Exiting the system...")
                break

            case 7:
                exprt_json()

            case _:
                print(f"{choice}, this is an invalid choice. Please try again.")


# _____________________________________________________
# Program starts here
# _____________________________________________________
if __name__ == "__main__":
    main()
