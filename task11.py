def analyze_list(items: list) -> dict:
    total = len(items)
    unique = 0
    dublicates = []
    most_common = items[0]

    for i in items:
        if items.count(i) == 1:
            unique += 1
        elif items.count(i) > 1 and i not in dublicates:
            dublicates.append(i)
        
        if items.count(most_common) < items.count(i):
            most_common = i
    
    dct = {
        'total': total,
        'unique': unique,
        'dublicates': dublicates,
        'most_common': most_common
    }

    return dct

print(analyze_list(["Ali", "Vali", "Ali", 1, 2, 1]))
