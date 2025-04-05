from stats import get_number_of_words, get_character_distribution, sorted_dictionary 


def get_book_text(book):
    textString = book.read()
    return textString





def main():
    with open("./books/frankenstein.txt") as f:
        book = get_book_text(f)

    print("============== BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(book)} total words")
    print("--------- Character Count -------")
    
    letter_dictionary = get_character_distribution(book)
    sorted_letters = sorted_dictionary(letter_dictionary)

    for letter in sorted_letters:
        if letter["name"].isalpha():
            print(f"{letter["name"]}: {letter["num"]}") 
        

main()



