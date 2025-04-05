def get_book_text(book):
    textString = book.read()
    return textString

def number_of_words(text):
    words = text.split()
    totalwords = 0
    for word in words:
        totalwords += 1

    return totalwords





def main():
    with open("./books/frankenstein.txt") as f:
        book = get_book_text(f)

    print(f"{number_of_words(book)} words found in the document")


main()



