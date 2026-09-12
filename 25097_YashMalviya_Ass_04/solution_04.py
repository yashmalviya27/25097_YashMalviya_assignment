# catalog = {"P01": {"price": 100.0, "stock": 5}, "P02": {"price": 50.0, "stock": 2}}

# order = {"P01": 5, "P02": 10}


# def process_order(catalog, order):
#     try:
#         error_01 = []

#         # Check whether every ordered product exists in catalog
#         for order_id in order:
#             if order_id not in catalog:
#                 error_01.append(order_id)
#                 raise ValueError(f"Product {order_id} is not in inventory.")
#         print(f"Code is running properly: {order=}")
#     except ValueError as e:
#         print(error_01, e)

#     try:
#         for catalog_id, catalog_detail in catalog.items():
#             aaa = catalog_detail[catalog.keys] -= order.calues()
            
    
#     except:
#         ...


# process_order(catalog, order)

# ```python
# Custom Exceptions

class ProductNotFoundError(Exception):
    pass


class OutOfStockError(Exception):
    pass


def process_order(catalog, order):

    # ---------------- VALIDATION PHASE ----------------

    # Check all products exist
    for product_id in order:
        if product_id not in catalog:
            raise ProductNotFoundError(
                f"Product '{product_id}' not found in store catalog."
            )

    # Check sufficient stock
    for product_id, quantity in order.items():

        available_stock = catalog[product_id]["stock"]

        if quantity > available_stock:
            raise OutOfStockError(
                f"Product '{product_id}' is out of stock. "
                f"Requested: {quantity}, Available: {available_stock}."
            )

    # ---------------- EXECUTION PHASE ----------------

    total = 0.0

    for product_id, quantity in order.items():

        price = catalog[product_id]["price"]

        # Deduct stock
        catalog[product_id]["stock"] -= quantity

        # Calculate cost
        total += price * quantity

    return total


# ---------------- TEST ----------------

catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}


# Successful order
try:
    total = process_order(catalog, {"P01": 2, "P02": 1})

    print("Order successful!")
    print("Total cost:", total)
    print("Catalog:", catalog)

except (ProductNotFoundError, OutOfStockError) as e:
    print("Order failed:", e)


# # Failed order
# try:
#     total = process_order(catalog, {"P01": 2, "P02": 15})

# except (ProductNotFoundError, OutOfStockError) as e:
#     print("Order failed:", e)

#     # Verify rollback
#     print("P01 stock:", catalog["P01"]["stock"])
#     print("P02 stock:", catalog["P02"]["stock"])

