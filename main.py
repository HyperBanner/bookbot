from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    filepath = "books/frankenstein.txt"
    book = get_book_text(filepath)
    word_count = get_word_count(book)
    char_count = get_char_count(book)
    sorted_count = sort_char_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_count:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")


main()
