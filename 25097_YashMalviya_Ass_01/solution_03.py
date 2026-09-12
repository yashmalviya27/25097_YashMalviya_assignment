def prime():
    num = int(input("Enter nun: "))
    half = num // 2
    for i in range(2, half):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number.")

prime()