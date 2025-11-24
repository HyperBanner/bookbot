import sys
from stats import get_book_text
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_count


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    word_count = get_word_count(book)
    sorted_count = sort_char_count(get_char_count(book))
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
