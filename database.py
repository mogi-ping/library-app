import sqlite3
from config import DB_NAME
from datetime import datetime
from models import Book, Borrowing


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    with open("sql/schema.sql", "r") as f:
        conn.executescript(f.read())
    conn.close()


# Books

def add_book(title, author):
    conn = get_connection()
    conn.execute(
        "INSERT INTO books (title, author) VALUES (?, ?)",
        (title, author)
    )
    conn.commit()
    conn.close()


def get_books():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM books")

    books = []
    for row in cursor.fetchall():
        books.append(Book(*row))

    conn.close()
    return books

def delete_book(book_id):
    conn = get_connection()

    # Cheking
    cursor = conn.execute("SELECT is_borrowed FROM books WHERE id = ?", (book_id,))
    result = cursor.fetchone()

    if not result:
        print("Книга не найдена")
        return

    if result[0]:
        print("Нельзя удалить выданную книгу")
        return

    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    print("Книга удалена")


# Give away

def borrow_book(book_id, user_name):
    conn = get_connection()

    cursor = conn.execute("SELECT is_borrowed FROM books WHERE id = ?", (book_id,))
    result = cursor.fetchone()

    if not result:
        print("Книга не найдена")
        return

    if result[0]:
        print("Книга уже выдана")
        return

    conn.execute(
        "INSERT INTO borrowings (book_id, user_name, borrow_date) VALUES (?, ?, ?)",
        (book_id, user_name, datetime.now().strftime("%Y-%m-%d"))
    )

    conn.execute(
        "UPDATE books SET is_borrowed = 1 WHERE id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()
    print("Книга выдана")


def return_book(book_id):
    conn = get_connection()

    cursor = conn.execute("SELECT is_borrowed FROM books WHERE id = ?", (book_id,))
    result = cursor.fetchone()

    if not result:
        print("Книга не найдена")
        return

    if not result[0]:
        print("Книга не была выдана")
        return

    conn.execute(
        "UPDATE borrowings SET return_date = ? WHERE book_id = ? AND return_date IS NULL",
        (datetime.now().strftime("%Y-%m-%d"), book_id)
    )

    conn.execute(
        "UPDATE books SET is_borrowed = 0 WHERE id = ?",
        (book_id,)
    )

    conn.commit()
    conn.close()
    print("Книга возвращена")


def get_borrowed_books():
    conn = get_connection()

    cursor = conn.execute("""
        SELECT br.id, br.book_id, br.user_name, br.borrow_date, br.return_date
        FROM borrowings br
        WHERE br.return_date IS NULL
    """)

    data = []
    for row in cursor.fetchall():
        data.append(Borrowing(*row))

    conn.close()
    return data

def search_books_by_author(author):
    conn = get_connection()

    cursor = conn.execute(
        "SELECT * FROM books WHERE author LIKE ?",
        (f"%{author}%",)
    )

    books = []
    for row in cursor.fetchall():
        books.append(Book(*row))

    conn.close()
    return books