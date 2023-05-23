import time
from random import randint

num = randint(1, 100)
#print(num)

print('Добро пожаловать в числовую угадайку!')
time.sleep(1)

def is_valid(num):
    if num not in [i for i in range(1, 101)]:
        return False
    else:
        return True

num2 = 0

while num2 == 0:
    a = int(input('Введите число от 1 до 100: '))
    if is_valid(a) == True:
        num2 = a
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue

while True:
    if num2 < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        time.sleep(2)
        num2 = int(input('Введите число от 1 до 100: '))
        continue
    elif num2 > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        time.sleep(2)
        num2 = int(input('Введите число от 1 до 100: '))
        continue
    elif num2 == num:
        print('Вы угадали, поздравляем')
        time.sleep(3)
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break