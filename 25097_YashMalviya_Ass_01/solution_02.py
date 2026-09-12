def Fibonacci():
    num = int(input("Enter the num: "))
    num01 = 0
    num02 = 1
    for _ in range(0, num):
        ans = num01 + num02
        print(ans)
        num02 = num01
        num01 = ans

Fibonacci()