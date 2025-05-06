def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def count_words(text):
    return len(text.split())


def count_letters(text):
    letters = {}

    for char in text.lower():
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    return letters


def sort_letters(letters_dict):
    letters_list = []

    for key, val in letters_dict.items():
        letters_list.append({"char": key, "num": val})

    letters_list.sort(key=lambda letter: letter["num"], reverse=True)
    return letters_list
