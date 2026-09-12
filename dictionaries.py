# this is how we create the Dictionaries
empty_dict_1 = {}
empty_dict_2 = dict()

# this is the another way to creat the Dictionaries
student = {"name": "Yash Malviya", "Age": 22, "course": "CSIT", "grades": [85, 90, 88]}

# 3. Using the dict() constructor with keyword arguments
employee = dict(name="Lisa", id=1042, department="R&D")

# 4. Using dict() with list of tuples (key-value pairs)
colors = dict([("red", "#FF0000"), ("green", "#00FF00"), ("blue", "#0000FF")])


# print("Student:", student)
# print("Employee:", employee)
# print("Colors:", colors)

# A. Bracket Notation (dict[key])
profile = {"username": "vinod_k", "role": "admin"}

# print(profile["username"])
email = profile.get("email")
print("Email:", email)

# Safe retrieval with custom default
email_with_default = profile.get("email", "no-email@example.com")
print("Email (with default):", email_with_default)
