import sys

from stats import chars_dict_to_sorted_list, count_character, count_words


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents

def print_report(
    path: str,
    word_count: int,
    char_count: list[tuple[str, int]]
) -> None:

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for key, count in char_count:
        print(f"{key}: {count}")
    print("============= END ===============")

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path: str = sys.argv[1]

    text = get_book_text(path)

    print_report(path, count_words(text), chars_dict_to_sorted_list(count_character(text)))


main()
