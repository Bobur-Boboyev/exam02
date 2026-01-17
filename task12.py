def sort_names(students: list) -> list:
    students = [i.title() for i in students]
    students.sort()
    return students

print(sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", 'azam']))
print(sort_names(["Zara", "Bobur", "Anvar"]))