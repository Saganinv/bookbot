from stats import get_word_count

def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(file):
    word_count = get_word_count(file)
    print(f"{word_count} words found in the document")

main("/home/sam/workspace/github.com/Saganinv/bookbot/books/frankenstein.txt")