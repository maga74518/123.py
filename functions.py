def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.readlines())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    pass


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    pass


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    pass