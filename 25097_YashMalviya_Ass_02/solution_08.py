# Exercise 8: Name Anonymizer
def name_anonymizer():
    name = input("Enter full name: ")
    name = name.split(" ")
    dump = []
    if len(name) == 1:
        print(name[0])
    else:
        for i in range(len(name) - 1):
            dump.append(name[i][0].upper() + ".")
        dump.append(name[-1])
        print(" ".join(dump))


name_anonymizer()
