# Exercise 6: Grading on a Curve
def grading():
    mark = "45 88 30 98 50"
    mark = mark.split(" ")
    mark = [int(i) for i in mark]
    score = [min(100, i + 10) if i < 50 else min(100, i + 5) for i in mark]
    print(f"""Original: {mark}
Curved: {score}""")


grading()
