from stats import count_words
from stats import character_count

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    char_counts = character_count(text)
    
    print(f"{num_words} words found in the document")
    print(char_counts)
    

    
if __name__ == "__main__":
    main()
    