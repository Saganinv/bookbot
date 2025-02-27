def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file):
    book_text = get_book_txt(file)
    words = book_text.split()
    return len(words)

def get_char_count(file):
    text = get_book_txt(file)
    lowecase_text = text.lower()
    character_count = {
        "a": lowecase_text.count("a"),
        "b": lowecase_text.count("b"),
        "c": lowecase_text.count("c"),
        "d": lowecase_text.count("d"),
        "e": lowecase_text.count("e"),
        "f": lowecase_text.count("f"),
        "g": lowecase_text.count("g"),
        "h": lowecase_text.count("h"),
        "i": lowecase_text.count("i"),
        "j": lowecase_text.count("j"),
        "k": lowecase_text.count("k"),
        "l": lowecase_text.count("l"),
        "m": lowecase_text.count("m"),
        "n": lowecase_text.count("n"),
        "o": lowecase_text.count("o"),
        "p": lowecase_text.count("p"),
        "q": lowecase_text.count("q"),
        "r": lowecase_text.count("r"),
        "s": lowecase_text.count("s"),
        "t": lowecase_text.count("t"),
        "u": lowecase_text.count("u"),
        "v": lowecase_text.count("v"),
        "w": lowecase_text.count("w"),
        "x": lowecase_text.count("x"),
        "y": lowecase_text.count("y"),
        "z": lowecase_text.count("z"),
    }
    return character_count