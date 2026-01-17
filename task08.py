def calculate_stats(numbers: list) -> dict:
    s = sum(numbers)
    average = round(s / len(numbers), 2) 
    dc = {'sum': s, 'average': average}
    return dc

print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))
print(calculate_stats([10, 20, 30]))