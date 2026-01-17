def find_pattern(items: list, pattern: str, match_type: str) -> list:
    if match_type == 'starts':
        items = list(
            filter(
                lambda i: i.lower().startswith(pattern.lower()),
                items
            )
        )
    elif match_type == 'ends':
        items = list(
            filter(
                lambda i: i.lower().endswith(pattern.lower()),
                items
            )
        )
    elif match_type == 'contains':
        items = list(
            filter(
                lambda i: pattern.lower() in i.lower(),
                items
            )
        )
    else:
        return "Error: Bunday pattern yuq"
    
    return items

print(find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts"))
print(find_pattern(["Alisher", "Bobur", "Jasur"], "ur", "ends"))
print(find_pattern(["Python", "Java", "JavaScript"], "java", "contains"))