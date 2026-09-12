def calculator():
    num1 = int(input("Enter the num 01: "))
    num2 = int(input("Enter the num 02: "))
    operator = input("Enter operator: ")

    if operator == "+":
        print(f"Result: {num1+num2}")
    elif operator == "-":
        print(f"Result: {num1-num2}")
    elif operator == "/":
        print(f"Result: {num1/num2}")
    elif operator == "*":
        print(f"Result: {num1*num2}")

calculator()