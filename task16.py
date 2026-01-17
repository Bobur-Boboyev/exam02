def count_by_grade(grades: dict, target_grade: int) -> dict:
    filtered_students = list(
        map(
            lambda student: student[0],
            filter(
                lambda student: student[1] == target_grade,
                grades.items()
            )
        )
    )
    count = len(filtered_students)

    dct = {
        'count': count,
        'students': filtered_students
    }

    return dct

print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))
print(count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4))