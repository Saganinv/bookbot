from stats import get_num_words, sort_on_char


def main():
    book_path = "/home/sam/workspace/github.com/Saganinv/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_dict = sort_on_char(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        if char.isalpha():
            print(f"{char}: {sorted_dict[char]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()