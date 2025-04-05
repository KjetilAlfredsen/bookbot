from stats import get_number_of_words, get_character_distribution 


def get_book_text(book):
    textString = book.read()
    return textString





def main():
        book = get_book_text(f)

    print("============== BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(book)} total words")
    print("--------- Character Count -------")
    
    letter_dictionary = get_character_distribution(book)

    for letter in letter_dictionary:
        number_of_letters = letter_dictionary[letter]
        print(f"'{letter}': {number_of_letters}")

main()



