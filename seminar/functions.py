def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as file:
        return print(file.read())

def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО')
    phone_num = input('Введите номер телефона')
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{fio} | {phone_num}')

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    pass


def search(book: str, info: str) -> str:
    """Находит в списке записи по определенному критерию поиска"""
    pass