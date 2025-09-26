def count_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char.isalpha() and "a" <= char <= "z":
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char, num in num_chars_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
