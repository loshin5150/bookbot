import sys
from stats import word_count, character_count, sort_dict

if (len(sys.argv)) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



def main():
    path = sys.argv[1]
    words = get_book_text(path)
    num_words = word_count(words)
    characters = character_count(words)
    sorted_characters = sort_dict(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dicti in sorted_characters:
        char = (dicti["char"])
        num = (dicti["num"])
        line = f"{char}: " + f"{num}"
        print(line)
    print("============= END ===============")

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

main()
