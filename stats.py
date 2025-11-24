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


def sort_on(items):
    return items["num"]


def sort_char_count(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "num": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
