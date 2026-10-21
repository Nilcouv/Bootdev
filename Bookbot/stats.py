def count_words(text):
    return len(text.split())

def count_character(text):
    characters = {}

    for c in text.lower():
        if c.isalpha():
            characters[c] = characters.get(c,0) + 1

    return characters

def sort_on(character: tuple[str, int]) -> int:
    return character[1]

def chars_dict_to_sorted_list(characters: dict[str, int]):
    char_list: list[tuple[str, int]] = []

    for key, count in characters.items():
        char_list.append((key,count))

    return sorted(char_list, reverse=True, key=sort_on)
