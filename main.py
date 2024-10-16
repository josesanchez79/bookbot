def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    counter = word_counter(text)
    lower_text = text.lower()
    char_count = char_counter(lower_text)
    char_list = char_dict_to_list(char_count)
    char_list = sort_char_list(char_list)
    print(f"--- Begin report of {book_path}")
    print(f"{counter} words found in the document")
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    

    print("--- End report ---")


def read_book(book_path):
    with open (book_path) as f:
        return f.read()
    
def word_counter(text):
    words = text.split()
    return len(words)

def char_counter(lower_text):
    char_dict = {}
    for char in lower_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def char_dict_to_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_on(dict):
    return dict["count"]

def sort_char_list(char_list):
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()