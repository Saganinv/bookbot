from stats import get_num_words, get_chars_dict, sort_on_char


def main():
    book_path = "/home/sam/workspace/github.com/Saganinv/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = sort_on_char(text)
    print(sorted_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()