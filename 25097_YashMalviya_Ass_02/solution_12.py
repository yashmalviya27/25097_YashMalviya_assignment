# Exercise 12: Date Validator & Pretty Formatter
def Date_Validator_Pretty_Formatter():

    try:
        date = input("Enter a valid date (eg-->>dd/mm/yyyy): ")
        date = [int(i) for i in date.split("/")]
        if len(date) != 3:
            print("Invalid Date!")
            return
        day = date[0]
        month_num = date[1]
        year = date[2]
        month = (
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )
        if month_num < 1 or month_num > 12:
            print("Invalid Date!")
            return
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            leap_year = True
        else:
            leap_year = False
        if month_num == 2:
            if leap_year:
                max_days = 29
            else:
                max_days = 28

        elif month_num in (4, 6, 9, 11):
            max_days = 30

        else:
            max_days = 31

        if day < 1 or day > max_days:
            print("Invalid Date!")
            return

        print(f"{month[month_num - 1]} {day:02d}, {year}")

    except ValueError:
        print("Invalid Date!")


Date_Validator_Pretty_Formatter()
