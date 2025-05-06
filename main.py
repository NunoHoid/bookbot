import sys

from stats import count_letters, count_words, get_book_text, sort_letters


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    count = count_words(book_text)
    letters = count_letters(book_text)
    letters = sort_letters(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for letter in letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


main()
