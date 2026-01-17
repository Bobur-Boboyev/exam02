from collections import Counter

def count_words(text: str) -> dict:
    text = text.lower().split()
    count = dict(Counter(text))
    return count

print(count_words("salom salom dunyo"))
print(count_words("Python python PYTHON"))