# STUDENT GRADE & ASSESSMENT MODULE
import json

# =============================this is user schema=========================================
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


# =========================Automated ID Logic===============================
def count_id():
    count = len(students)
    return count


# ==================Automated Grade Evaluation Logic========================
def grade_evaluation(marks: int):
    if marks >= 85.0 and marks < 100:
        return "A"
    elif marks >= 70.0 and marks < 85:
        return "B"
    elif marks >= 50.0 and marks < 70:
        return "c"
    elif marks > 00 and marks < 50:
        return "f"
    else:
        return f"No negative mark is accepted."


# ======================this is Menu of the project=========================
def menu():
    text = """[1] Enroll Student
[2] Cohort Directory
[3] Query Records
[4] Revise Evaluation
[5] Purge Record
[6] Saveto JSON
[7] Load from JSON
[8] Terminate"""
    print("-" * 60)
    print("============STUDENT GRADE & ASSESSMENT MODULE============")
    print("-" * 60)
    print(f"{text}")
    print("-" * 60)
    try:
        choice = int(input("enter the choice under 1 to 8: "))
        return choice
    except ValueError:
        print("No nagitave and char is acepted.")


# ============================this is add module============================
def student_enrollment():
    enrol = {}
    # ====this is for add "NAme"====
    while True:
        name_ = input("Name: ").strip().title()
        if not name_.replace(" ", "").isalpha():
            print("Please reenter the Name.")
        else:
            break
    # ====this is for adding the "course"====
    while True:
        course_ = input("Course: ").strip().title()
        if not course_.replace(" ", "").isalpha():
            print("Please reenter the Course.")
        else:
            break
    # ====this is for adding the mark====
    while True:
        try:
            mark_ = float(input("Mark: "))
            if mark_ == " ":
                print("mark not be empty")
            elif mark_ < 0:
                print("Mark not be negative")
            else:
                break
        except ValueError:
            print("Mark must be digit.")

    enrol = {
        "id": count_id(),
        "name": name_,
        "course": course_,
        "marks": mark_,
        "grade": grade_evaluation(mark_),
    }
    print(enrol)
    students.append(enrol)


# ========================this is gor display the user========================
def display_cohort():
    if len(students) == 0:
        print("No user found.!")
    elif len(students) == 1:
        print("=" * 60)
        print("======Student is======")
        print("=" * 60)
        print(f"""ID     : {students[0]['id']}
Name   : {students[0]['name']}
Course : {students[0]['course']}
Marks  : {students[0]['marks']}
Grade  : {students[0]['grade']}""")
        print("=" * 60)
    else:
        print("=" * 50)
        print(f"{'ID':^5}{'Name':<15}{'Course':<10}{'Marks':>10}{'Grade':>10}")
        print("=" * 50)
        for student in students:
            id_, name_, course_, marks_, grade_ = student.values()
            print(f"{id_:^5}{name_:<15}{course_:<10}{marks_:>10.2f}{grade_:>10}")
            print("=" * 50)


# ========================this is gor delet the user========================
def delet_student():
    try:
        user_id = int(input("ID: "))
        for student in students:
            if user_id == student["id"]:
                print(f"""ID     : {student['id']}
Name   : {student['name']}
Course : {student['course']}
Marks  : {student['marks']}
Grade  : {student['grade']}""")
                yes_no = input("Entrt the y/n").strip().title()
                if yes_no == "Y":
                    students.remove(student)
                    print("Student deleted succesfully")
                    break
                else:
                    print("Student is not deleted")

    except ValueError:
        print("Enter the correct id")


# ========================this is gor delet the user========================
def sev_json():
    try:
        students_ = "student.json"
        with open(students_, "wt") as file:
            json.dump(students_, file, indent=5)
    except Exception:
        print("there is an unwanted error")


def load_from_json():

    print("\n" + "=" * 60)
    print("                    LOAD FROM JSON")
    print("=" * 60)

    try:

        with open("students.json", "r") as file:

            loaded_students = json.load(file)

        # Replace current records
        students.clear()
        students.extend(loaded_students)

        print("Student records successfully loaded from students.json.")

    except FileNotFoundError:

        print("students.json file does not exist.")

    except json.JSONDecodeError:

        print("students.json contains invalid JSON.")

    except OSError as error:

        print(f"Error while reading file: {error}")



def main():
    while True:
        match menu():
            case 1:
                student_enrollment()
            case 2:
                display_cohort()
            case 5:
                delet_student()
            case 6:
                sev_json()
            case 7:
                load_from_json()
            case 8:
                break
            case _:
                print("Choice under 1 to 8 not more then 8 and less then 1")


if __name__ == "__main__":
    main()
