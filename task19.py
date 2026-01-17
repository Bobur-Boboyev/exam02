def find_longest_name(names: list) -> str:
    longest_name = max(names, key = lambda name: len(name))
    return longest_name

print(find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad']))
print(find_longest_name(['Bo', 'Ali', 'Zara']))