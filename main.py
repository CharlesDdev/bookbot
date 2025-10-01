import sys
from pathlib import Path

from stats import count_words, character_count, chars_dict_to_sorted_list

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = Path(sys.argv[1])
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = character_count(text)
    sorted_char_counts = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
if __name__ == "__main__":
    main()
    
