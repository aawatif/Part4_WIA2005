def find_book(filename, title):
    with open(filename, "r") as file:
        for i, book_title in enumerate(file):
            if book_title.strip() == title:
                return i

    return -1


title_to_find = input("Enter the title of the book: ")
file_name = "book_list.txt"

book_index = find_book(file_name, title_to_find)

if book_index != -1:
    print("\nBook found at line", book_index + 1)
else:
    print("Book not found in the collection")
