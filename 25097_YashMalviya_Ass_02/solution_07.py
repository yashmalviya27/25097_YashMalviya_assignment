# Exercise 7: Manual Substring Counter
def manual_substring_counter():
    main_text = input("Enter main text: ")
    substring = input("Enter substring: ")
    count = 0
    for i in range(len(main_text) - len(substring) + 1):
        if main_text[i : i + len(substring)] == substring:
            count += 1

    print("Count:", count)


manual_substring_counter()