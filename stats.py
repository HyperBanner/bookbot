def get_word_count(book):
    split_list = book.split()
    return len(split_list)


def get_char_count(book):
    char_dict = {}
    for char in book.lower():
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
