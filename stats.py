def get_number_of_words(text):
    words = text.split()
    totalwords = 0
    for word in words:
        totalwords += 1

    return totalwords

def get_character_distribution(text):
    text = text.lower()
    dictionary_of_words = {}
    for letter in text:
        if (f"{letter}" in dictionary_of_words):
            dictionary_of_words[f"{letter}"] += 1
        else:
            dictionary_of_words[f"{letter}"] = 1

    return dictionary_of_words



