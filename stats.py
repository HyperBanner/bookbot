def get_num_words(string):
    return len(string.split())

def get_num_chars(string):
    counted = {}
    for char in string:
        char = char.lower()
        if char not in counted:
            counted[f"{char}"] = 1
        else:
            counted[f"{char}"] += 1
    return counted

def sort_on(dictionary):
    return dictionary["count"]

def get_sorted_dicts(dictionary):
    sorted_dicts = []
    for char, count in dictionary.items():
        sorted_dicts.append({"character": char, "count": count})
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
