def count_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts