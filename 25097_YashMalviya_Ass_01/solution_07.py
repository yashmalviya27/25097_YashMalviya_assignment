def multiplication_table():
    num = int(input("Enter the num: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

multiplication_table()