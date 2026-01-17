def find_shortest_name_student(students: list) -> str:
    shortest_name = min(students, key = lambda student: len(student['name']))['name']
    return shortest_name


students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
print(find_shortest_name_student(students))
students2 = [
    {'name': 'Jo', 'age': 19},
    {'name': 'Ali', 'age': 20},
    {'name': 'Bob', 'age': 18}
]
print(find_shortest_name_student(students2))