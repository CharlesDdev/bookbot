from stats import count_words

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    text = get_book_text('books/frankenstein.txt')
    num_words = count_words(text)
    
    print(f"{num_words} words found in the document")
    

    
if __name__ == '__main__':
    main()
    