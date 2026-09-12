# Exercise 5: Custom Title Case Formatter
def custom_title_case_formatter():
    data = input("Ensert the data: ")
    word = data.split(" ")
    dump = []
    for word in word:
        formatted_word = word[0].upper() + word[1:].lower()
        dump.append(formatted_word)

    print(" ".join(dump))


custom_title_case_formatter()
