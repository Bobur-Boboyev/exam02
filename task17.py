def filter_positive(numbers: list) -> list:
    filtered_numbers = list(
        filter(
            lambda num: num['value'] > 0,
            numbers
        )
    )
    return filtered_numbers

print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))
print(filter_positive([{'value': 0}, {'value': 5}, {'value': -3}]))