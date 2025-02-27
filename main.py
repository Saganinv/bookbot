from stats import get_word_count
from stats import get_char_count

def main(file):
    word_count = get_word_count(file)
    char_count = get_char_count(file)
    print(f"{word_count} words found in the document")
    print(char_count)

main("/home/sam/workspace/github.com/Saganinv/bookbot/books/frankenstein.txt")