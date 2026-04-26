class Book:
    def __init__(self, id, title, author, is_borrowed):
        self.id = id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        status = "Выдана" if self.is_borrowed else "Доступна"
        return f"{self.id} | {self.title} | {self.author} | {status}"


class Borrowing:
    def __init__(self, id, book_id, user_name, borrow_date, return_date):
        self.id = id
        self.book_id = book_id
        self.user_name = user_name
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __str__(self):
        return f"{self.book_id} | {self.user_name} | {self.borrow_date}"