import json
students = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "course": "Python Core",
        "marks": 88.5,
        "grade": "A",
    },
    {
        "id": 2,
        "name": "Diya Patel",
        "course": "Data Science",
        "marks": 74.0,
        "grade": "B",
    },
]

# file_name = "yash_01.txt"

# with open(file_name, "wt") as file:
#     for c in students:
#         id, name, course, marks, grade = c.values()
#         file.write(f"{id};{name};{course}:{marks}:{marks}\n")
# with open(file_name, "r") as file:
#     data =file.read()
#     print(data)



# with open(file_name, "w") as file:
#     data = json.dump(students,file, indent=4)
#     print(data)
# with open(file_name, "r") as file:
#     data = json.load(file)
#     print(data)


import csv

file_name = "students.csv"

# Write
with open(file_name, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=students[0].keys())
    writer.writeheader()
    writer.writerows(students)

# Read
with open(file_name, "r", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

print(data)

