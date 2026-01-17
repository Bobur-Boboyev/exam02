def sort_numbers(numbers: list, reverse: bool = False) -> list:
    numbers.sort(reverse=reverse)
    return numbers

print(sort_numbers([3, 7, 10, -5, -8, 15, 22, 0]))
print(sort_numbers([3, 7, 10, -5], reverse=True))