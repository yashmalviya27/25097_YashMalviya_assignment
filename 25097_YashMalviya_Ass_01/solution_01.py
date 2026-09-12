def leap():
    date = int(input("Enter year to check weather the year is leap year or not: "))
    if date % 4 == 0 or date % 400 == 0:
        print(f"{date} is a leap year")
    else:
        print(f"{date} is not an leap year.")










