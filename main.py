def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(file):
    book_text = get_book_txt(file)
    print(book_text)

main("/home/sam/workspace/github.com/Saganinv/bookbot/books/frankenstein.txt")