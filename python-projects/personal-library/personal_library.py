import json
import os

data_file = "library.txt"

def load_library():
    if os.path.exists(data_file):
        try:
            with open(data_file, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error reading library file. Starting with an empty library.")
            return []
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter a book title: ")
    author = input("Enter the author: ")
    publication_year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    isRead = input("Have you read this book? (yes/no): ").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": publication_year,
        "genre": genre,
        "isRead": isRead
    }

    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully.\n")

def remove_book(library):
    title = input("Enter the title of the book to remove from the library: ").lower()
    initial_length = len(library)
    updated_library = [book for book in library if book["title"].lower() != title]

    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f"Book '{title}' removed successfully.\n")
        return updated_library
    else:
        print(f"Book '{title}' not found in the library.\n")
        return library

def search_library(library):
    search_by = input("Search by 'title' or 'author': ").lower()
    if search_by not in ["title", "author"]:
        print("Invalid search field.\n")
        return

    search_term = input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book["isRead"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        print()
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.\n")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book["isRead"] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
        print()
    else:
        print("The library is empty.\n")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["isRead"])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%\n")

def main():
    library = load_library()
    while True:
        print("Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            library = remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
