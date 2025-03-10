import sys
from stats import get_num_words, get_num_chars, get_sorted_dicts

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    file_contents = get_book_text(f"{sys.argv[1]}")
    word_count = get_num_words(file_contents)
    char_count = get_num_chars(file_contents)
    sorted_dicts = get_sorted_dicts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_dicts:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["count"]}")
    print("============= END ===============")


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
