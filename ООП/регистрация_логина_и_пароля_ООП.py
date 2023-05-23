forbidden = ['123456', '124244242', 'password', '123456789', '12345', '12345678', 'qwerty', '1234567', '111111',
             '1234567890',
             '123123', 'abc123', '1234', 'password1', 'iloveyou', '1q2w3e4r', '000000', 'qwerty123', 'zaq12wsx',
             'dragon', 'sunshine', 'princess', 'letmein', '654321', 'QwerTy123', 'KissasSAd1f', 'monkey', '27653',
             '1qaz2wsx', '123321', 'qwertyuiop', 'superman', 'asdfghjkl']


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Логин должен содержать один символ '@'")
        elif '.' not in value or value.index('@') > value.index('.'):
            raise ValueError("Логин должен содержать символ '.'")
        else:
            self.__login = value

    @staticmethod
    def is_include_all_register(value):
        return (any(map(str.isupper, value)) != True) and (any(map(str.islower, value)))

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if type(value) != str:
            raise TypeError("Пароль должен быть строкой")
        elif len(value) not in list(range(5, 12)):
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        elif any(map(str.isdigit, value)) != True:
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        elif value in forbidden:
            raise ValueError('Ваш пароль содержится в списке самых легких')

    @staticmethod
    def is_include_only_latin(value):
        if any(map(str.islower, value)) != True and any(map(str.isupper, value)) != True:
            raise ValueError('Пароль должен содержать только латинский алфавит')
