def filter_long_names(students: list, min_length: int = 5) -> list:
    filtered_students = list(
        filter(
            lambda student: len(student) >= min_length,
            students
        )
    )
    return filtered_students

print(filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"]))
print(filter_long_names(["Ali", "Muhammad", "Jo"], 4))