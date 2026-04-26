from database import *
from utils import *


def menu():
    init_db()

    while True:
        print("\n=== Библиотека ===")
        print("1. Добавить книгу")
        print("2. Показать каталог")
        print("3. Выдать книгу")
        print("4. Вернуть книгу")
        print("5. Выданные книги")
        print("6. Удалить книгу")
        print("7. Поиск по автору")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            add_book(title, author)

        elif choice == "2":
            books = get_books()
            print_books(books)

        elif choice == "3":
            book_id = safe_int_input("ID книги: ")
            if book_id is None:
                continue
            user = input("Имя читателя: ")
            borrow_book(book_id, user)

        elif choice == "4":
            book_id = safe_int_input("ID книги: ")
            if book_id is None:
                continue
            return_book(book_id)

        elif choice == "5":
            data = get_borrowed_books()
            print_borrowed(data)

        elif choice == "6":
            book_id = safe_int_input("ID книги: ")
            if book_id is None:
                continue
            delete_book(book_id)

        elif choice == "7":
            author = input("Введите автора: ")
            books = search_books_by_author(author)
            print_books(books)

        elif choice == "0":
            break

        else:
            print("Ошибка ввода")


if __name__ == "__main__":
    menu()