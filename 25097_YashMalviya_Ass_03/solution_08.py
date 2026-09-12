# Exercise 8: De-duplicating Shopping Cart
def De_duplicating_Shopping_Cart():
    shopping_cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    cleaned_cart = []
    [cleaned_cart.append(i) for i in shopping_cart if i not in cleaned_cart]
    print(cleaned_cart)


De_duplicating_Shopping_Cart()
