def compile_feedback(ratings_dict):
    compile_data = {}

    for course, rating in ratings_dict.items():
        rated_data = []
        for rate in rating:
            try:
                num = float(rate)
                rated_data.append(num)
            except :
                print(
                    f"Warning: Invalid rating value '{rate}' in course '{course}' skipped."
                )
        try:
            avg = sum(rated_data) / len(rated_data)
            compile_data[course] = round(avg, 2)
        except ZeroDivisionError:
            print(f"No valid ratings found for course '{course}'. Rating set to 0.0.")
            compile_data[course] = 0.0
    return compile_data


feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None],
}

compiled_feedback = compile_feedback(feedback_data)
print("\nCompiled Feedback:")
print(compiled_feedback)
