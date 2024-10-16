def main():

    #assigning needed variables
    book_path = "books/frankenstein.txt"
    text = read_book(book_path) #use of read_book to take frankenstein.txt
    counter = word_counter(text) #use of word_counter to count words
    lower_text = text.lower() #text lowered as specified on project
    char_count = char_counter(lower_text) #counting char count of each char in the book
    char_list = char_dict_to_list(char_count) #function to convert char dictionary to a list
    char_list = sort_char_list(char_list) #char list is iterated using sort_char_list

    #Begin report
    print(f"--- Begin report of {book_path}")
    print(f"{counter} words found in the document")
    #loop used to loop over sort char list in order to print
    for char in char_list:
        print(f"The '{char['char']}' character was found {char['count']} times")
    

    print("--- End report ---")

#function to read text from file in path
def read_book(book_path):
    with open (book_path) as f:
        return f.read()

#this function takes the string, split it and return length of the string
def word_counter(text):
    words = text.split()
    return len(words)

#this function takes the lower_text string, loops over it and counts how many times a character shows up, return a dictionary
def char_counter(lower_text):
    char_dict = {}
    for char in lower_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

#converts dictionary to a list of dictionaries
def char_dict_to_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    return char_list

#stablishes that for each dict on the list, we'll use "count" value for sorting
def sort_on(dict):
    return dict["count"]

#sorts list in reverse to count from highest to lowest number, using key="count" value to determine the order
def sort_char_list(char_list):
    char_list.sort(reverse=True, key=sort_on)
    return char_list

main()