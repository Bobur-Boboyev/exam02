def find_top_students(grades: dict) -> dict:
    max_grade = max(grades.items(), key = lambda x: x[1])[1]
    students = list(
        map(
            lambda student: student[0],
            filter(
                lambda student: student[1] == max_grade,
                grades.items()
            )
        )
    )
    
    dct = {
        "max_grade": max_grade,
        "students": students
    }
    return dct

print(find_top_students({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}))
print(find_top_students({"Aziz": 4, "Bobur": 5, "Diyor": 3}))