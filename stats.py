from main import get_book_txt

def get_word_count(file):
    book_text = get_book_txt(file)
    words = book_text.split()
    return len(words)