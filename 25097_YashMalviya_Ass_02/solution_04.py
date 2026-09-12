# Part B: Medium Complexity (5 Exercises)
#
# Exercise 4: Vowel & Consonant Frequency


def vowel_consonant_frequency():
    string = input("Enter the string: ").strip()
    a, e, i, o, u, consonants = 0, 0, 0, 0, 0, 0
    for vowel in string:
        if "a" == vowel:
            a += 1
        elif "e" == vowel:
            e += 1
        elif "i" == vowel:
            i += 1
        elif "o" == vowel:
            o += 1
        elif "u" == vowel:
            u += 1
        else:
            consonants += 1

    print(f"""Vowel Frequencies:
a: {a}
e: {e}
i: {i}
o: {o}
u: {u}
Total Consonants: {consonants}""")


vowel_consonant_frequency()
