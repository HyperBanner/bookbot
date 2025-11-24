from stats import get_word_count
from stats import get_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book)
    char_count = get_char_count(book)
    print(f"Found {word_count} total words")
    print(char_count)


main()
