def score_to_grade_converter():
    mark = int(input("Enter your mark: "))
    if mark > 90 and mark < 101:
        print(f"Grade: A")
    if mark > 79 and mark < 90:
        print(f"Grade: B")
    if mark > 69 and mark < 80:
        print(f"Grade: C")
    if mark > 0 and mark < 61:
        print(f"Grade: F")
    else:
        print("Invalid num you entered.")


score_to_grade_converter()