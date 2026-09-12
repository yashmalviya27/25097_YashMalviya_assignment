# Assignment 1: CDAC Cafeteria Discount Calculator
def calculate_cafeteria_bill(
    base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0
):
    raw_subtotal = base_price + sum(items)
    discounted_subtotal = raw_subtotal * (1 - discount / 100)
    tax = discounted_subtotal * tax_rate
    final_total = discounted_subtotal + tax + delivery_fee
    return round(final_total, 2)


def main():
    total1 = calculate_cafeteria_bill(100.0)
    print("Total 1:", total1)

    total2 = calculate_cafeteria_bill(
        100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0
    )

    print("Total 2:", total2)


main()
