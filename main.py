def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    counter = word_counter(text)
    print(f"{text}, the word count is: {counter}")
    lower_text = text.lower()
    char_count = char_counter(lower_text)
    print(char_count)

def read_book(book_path):
    with open (book_path) as f:
        return f.read()
    
def word_counter(text):
    return len(text)

def char_counter(lower_text):
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()