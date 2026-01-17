def find_min_max(numbers: list) -> dict:
    mn = min(numbers)
    mx = max(numbers)

    dct = {
        'max': mx,
        'min': mn
    }
    return dct

print(find_min_max([3, 7, 10, -5, -8, 15, 22]))
print(find_min_max([100, 50, 200, -10]))