def word_count(file_contents):
    num_words = file_contents.split()
    return len(num_words)

def character_count(file_contents):
    char_dict = {}
    lower = file_contents.lower()
    for char in lower:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dictionary):
    dict_list = []
    for letter in dictionary:
        if letter.isalpha():
            letter = {"char": letter, "num": (dictionary[letter])}
            dict_list.append(letter)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
