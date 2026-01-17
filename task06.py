def analyze_grades(students: dict) -> dict:
    total_grade = sum(students.values())
    average = total_grade / len(students)
    above_average = list(
        map(
            lambda student: student[0],
            filter(
                lambda student: student[1] > average,
                students.items()
            )
        )
    )
    dct = {
        "average": average,
        "above_average": above_average
    }
    return dct

print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))
print(analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5}))