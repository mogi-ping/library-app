def print_books(books):
    if not books:
        print("Нет книг")
        return

    for b in books:
        print(b)


def print_borrowed(data):
    if not data:
        print("Нет выданных книг")
        return

    for d in data:
        print(d)


def safe_int_input(message):
    try:
        return int(input(message))
    except ValueError:
        print("Введите число")
        return None