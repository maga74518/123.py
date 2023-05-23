class File:

    def __init__(self, name):
        self.name = name
        self.is_deleted = False
        self.in_trash = False

    def restore_from_trash(self):
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted == True:
            return print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash == True:
            return print(f'ErrorReadFileTrashed({self.name})')
        print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            return print(f'ErrorWriteFileDeleted({self.name})')
        if self.in_trash:
            return print(f'ErrorWriteFileTrashed({self.name})')
        print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []
    @staticmethod
    def add(file):
        if isinstance(file, File):
            Trash.content.append(file)
            file.in_trash = True
        else:
            print('В корзину добавлять можно только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for i in Trash.content:
            File.remove(i)
        Trash.content = []
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for i in Trash.content:
            i.restore_from_trash()
        Trash.content = []
        print('Корзина пуста')

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() # после этой команды вывод должен быть таким
'''
Очищаем корзину
Файл puppies.jpg был удален
Файл cat.jpg был удален
Файл pass.txt был удален
Корзина пуста
'''

f1.read() # ErrorReadFileTrashed(puppies.jpg)
f1.in_trash = False
print(f1.__dict__)