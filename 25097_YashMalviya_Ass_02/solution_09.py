# Part C: Difficult Complexity (2 Exercises)
# Exercise 9: Longest Palindromic Substring
def longest_palindromic():
    data = input("Enter Data: ")
    dump = ""
    for i in range(len(data) + 1):
        for j in range(i + 1, len(data) + 1):
            sub = data[i:j]
            print(sub)
            if sub == sub[::-1]:
                if len(sub) > len(dump):
                    dump = sub
    print("Longest palindrome:", dump)


longest_palindromic()
