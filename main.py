import sys
from stats import get_words
from stats import lett_count , build_sorted_list
    
def main():
    input = len(sys.argv)
    if input != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        letters = lett_count(text)
        sorted_chars = build_sorted_list(letters)
        wordcount = get_words(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

