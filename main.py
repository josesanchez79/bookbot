def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        print(file_contents)

def count_words(file_contents):
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    print(counter)
    return counter


main()

book_read = main()
count_words(book_read)