def count_words(text):
    return len(text.split())

def character_count(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_on(char_dict):
    """Return the numeric count from a character-count dictionary."""

    return char_dict["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """Convert the counts dictionary into a sorted list of dictionaries.

    The resulting list is ordered from the most frequent character to the
    least frequent, with each entry containing the character and its count.
    """

    sorted_list = []
    for char, num in num_chars_dict.items():
        sorted_list.append({"char": char, "num": num})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
