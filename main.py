from stats import count_letters, count_words, get_book_text


def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    count = count_words(frankenstein)
    print(f"{count} words found in the document")
    letters = count_letters(frankenstein)
    print(letters)


main()
