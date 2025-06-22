import sys
from stats import *

# Step 1: Check argument count
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)  # Exit with error code 1

# Step 2: Use the book path from command line
book_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as file_used:
        text = file_used.read()
    return text

def main():
    book_text = get_book_text(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(book_text)} total words")
    
    print("--------- Character Count -------")
    char_dict = character_count(book_text)
    for item in sorted_dictionary(char_dict):
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()








