def square_values(numbers: list) -> list:
    squared_numbers = list(
        map(
            lambda num: {'value': num['value'] ** 2},
            numbers
        )
    )
    return squared_numbers

print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))
print(square_values([{'value': -2}, {'value': 5}]))