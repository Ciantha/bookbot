def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = book_num_words(text)
    letter_count = count_letters(text)
    create_book_report(book_path, num_words, letter_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def book_num_words(text):
    word_list = text.split()
    return len(word_list)

def count_letters(text):
    letter_dictionary = {}
    text = text.lower()

    for char in text:
        if char in letter_dictionary:
            letter_dictionary[char] += 1
        else:
            letter_dictionary[char] = 1
    return letter_dictionary

def create_book_report(path, num_words, letter_count):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()

    letter_list = list(letter_count.items())
    letter_list = sorted(letter_list, key=lambda letter : letter[1], reverse = True)
    #print(letter_list[1][1])
    for letter in letter_list:
        if letter[0].isalpha():
            print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")

    


main()