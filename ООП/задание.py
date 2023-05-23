from collections import defaultdict

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class User:
    def __init__(self, login, balance=0):
        self.__login = login
        self.__balance = balance

    def __str__(self):
        return f"Пользователь {self.__login}, баланс - {self.__balance}"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        self.__balance += amount

    def payment(self, amount):
        if self.__balance < amount:
            print("Не хватает средств на балансе. Пополните счет")
            return False
        else:
            self.__balance -= amount
            return True

class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = defaultdict(int)
        self.__total = 0

    def add(self, product, quantity=1):
        self.goods[product] += quantity
        self.__total += product.price * quantity

    def remove(self, product, quantity=1):
        if self.goods[product] <= quantity:
            del self.goods[product]
            self.__total -= product.price * quantity
        else:
            self.goods[product] -= quantity
            self.__total -= product.price * quantity


    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print("Заказ оплачен")
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print("---Your check---")
        for product, quantity in sorted(self.goods.items(), key=lambda x: x[0].name):
            total_price = product.price * quantity
            print(f"{product.name} {product.price} {quantity} {total_price}")
        print(f"---Total: {self.total}---")


billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user) # Пользователь billy@rambler.ru, баланс - 0
cart_billy.add(lemon, 2)
cart_billy.add(carrot)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 2 40
---Total: 70---'''
cart_billy.add(lemon, 3)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.remove(lemon, 6)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
---Total: 30---'''
print(cart_billy.total) # 30
cart_billy.add(lemon, 5)
cart_billy.print_check()
''' Печатает текст ниже
---Your check---
carrot 30 1 30
lemon 20 5 100
---Total: 130---'''
cart_billy.order()
''' Печатает текст ниже
Не хватает средств на балансе. Пополните счет
Проблема с оплатой'''
cart_billy.user.deposit(150)
cart_billy.order() # Заказ оплачен
print(cart_billy.user.balance) # 20