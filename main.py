from stats import get_number_of_words, get_character_distribution, sorted_dictionary
import sys


def get_book_text(book):
    textString = book.read()
    return textString





def main():
    if len(sys.argv) != 2:
        prinf("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(f"{sys.argv[1]}") as f:
        book = get_book_text(f)

    print("============== BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(book)} total words")
    print("--------- Character Count -------")
    
    letter_dictionary = get_character_distribution(book)
    sorted_letters = sorted_dictionary(letter_dictionary)

    for letter in sorted_letters:
        if letter["name"].isalpha():
            print(f"{letter["name"]}: {letter["num"]}") 
        

main()



