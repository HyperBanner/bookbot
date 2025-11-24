def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def get_word_count(book):
    split_list = book.split()
    return len(split_list)


def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(book)
    print(f"Found {word_count} total words")


main()
