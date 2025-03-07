# Задача: Система учета студентов
# Создайте класс Student, который будет хранить информацию о студенте и его оценках. Реализуйте следующие возможности:
# Хранение имени, возраста и списка оценок студента.
# Метод для добавления новой оценки.
# Метод для вычисления среднего балла.
# Метод для определения, является ли студент отличником (средний балл >= 4.5).
from itertools import product


# class Student:
#     def __init__(self, name, age, faculty):
#         self.name = name
#         self.age = age
#         self.faculty = faculty
#         self.grades = []
#
#     def add_grade(self, grades):
#         if not isinstance(grades, int):
#             raise ValueError("Error! Use numbers!")
#         if grades > 0 and grades <= 5:
#             self.grades.append(grades)
#         else:
#             raise ValueError("Wrong value! Enter numbers(1-5)")
#
#     def get_avarage_grade(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#     def is_exellent(self):
#         return self.get_avarage_grade() >= 4.5
#
# stud1 = Student("Vasily Pupkin", 21, "Law")
# stud1.add_grade(3)
# stud1.add_grade(5)
# stud1.add_grade(3)
# stud1.add_grade(4)
# print(f"{stud1.name}, {stud1.age}, Faculty: {stud1.faculty},"
#       f" has avarage grade: {stud1.get_avarage_grade()}, Exellent grade: {stud1.is_exellent()}")
#
# stud2 = Student("Ivan Bocharov", 23, "Medic")
# stud2.add_grade(4)
# stud2.add_grade(5)
# stud2.add_grade(5)
# stud2.add_grade(4)
# print(f"{stud2.name}, {stud2.age}, Faculty: {stud2.faculty},"
#       f" has avarage grade: {stud2.get_avarage_grade()}, Exellent grade: {stud2.is_exellent()}")


# Задача: Библиотечная система

# Создайте класс Book, который будет моделировать книгу в библиотеке. Реализуйте следующие возможности:
#
# Хранение названия книги, автора и года издания.
# Метод для "взятия книги" (отмечает, что книга взята, если она доступна).
# Метод для "возврата книги" (отмечает, что книга снова доступна).
# Метод для проверки, доступна ли книга в данный момент.

# При создании книги она должна быть изначально доступна.
# Если кто-то пытается взять уже взятую книгу, должно выводиться сообщение об ошибке.
# Аналогично, если пытаются вернуть книгу, которая не была взята, тоже должно быть сообщение.
# Пример использования (ожидаемое поведение):
# class Book:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#         self.status = True
#
#     def is_available(self):
#         return self.status
#
#     def take_book(self):
#         if self.status == True:
#             self.status = False
#             print(f"Book {self.name} taken")
#         else:
#             print(f"Error! Book {self.name} is already taken!")
#
#     def return_book(self):
#         if self.status == False:
#             self.status = True
#             print(f"Book {self.name} was returned")
#         else:
#             print(f"Error! Book {self.name} is already returned")
#
#
# book = Book("Война и мир", "Лев Толстой", 1865)
# print(book.is_available())  # True
# book.take_book()           # "Книга 'Война и мир' взята"
# book.take_book()           # "Ошибка: книга уже взята"
# book.return_book()         # "Книга 'Война и мир' возвращена"
# print(book.is_available())  # True

# Задача: Система учета заказов в кафе
# Создайте класс Order, который будет моделировать заказ в кафе. У заказа есть определённые свойства и методы для управления его состоянием.
#
# Свойства:
# Номер заказа — уникальный идентификатор (целое число).
# Список блюд — список названий блюд в заказе (например, ["Кофе", "Бургер"]).
# Статус заказа — строка, которая может быть "принят", "готовится" или "выдан".
# Общая стоимость — число с плавающей точкой, сумма цен всех блюд.

# class Order:
#     def __init__(self, order_number):
#         self.order_number = order_number
#         self.status = "принят"
#         self.total_sum = 0.0
#         self.dish_list = []
#
#     def add_dish(self, dish_name, price):
#         if self.status != "выдан":
#             self.dish_list.append((dish_name, price))
#             self.total_sum += price
#             print(f"Блюдо/Напиток '{dish_name}' добавлено к заказу '№{self.order_number}' ")
#         else:
#             print("Блюдо уже выдано!")
#
#     def change_status(self, new_status):
#         valid_statuses = ["принят", "готовится", "выдан"]
#         if new_status in valid_statuses:
#             self.status = new_status
#             print(f"Статус заказа '№{self.order_number}' изменен на '{new_status}'")
#         else:
#             print("Ошибка! Недопустимый статус!")
#
#     def get_total_price(self):
#          print(f"Общая стоимость заказа: ", self.total_sum)
#
#     def is_completed(self):
#         return self.status == "выдан"
#
# my_order1 = Order(1)
# my_order1.add_dish("Кофе", 10)
# my_order1.add_dish("Пиво", 20)
# my_order1.get_total_price()
# my_order1.change_status("выдан")
# print(f"Заказ выдан: {my_order1.is_completed()}")
# my_order1.change_status("выдан")
# print(f"Заказ '№{my_order1.order_number}', статус '{my_order1.status}', список заказа: {my_order1.dish_list},"
#       f" Итоговая сумма: {my_order1.total_sum} ")
#
# my_order2 = Order(2)
# my_order2.add_dish("Currywurst", 50)
# my_order2.add_dish("Bier", 40)
# my_order2.change_status("выдан")
# my_order2.get_total_price()
# my_order2.change_status("готовится")
# print(f"Заказ выдан: {my_order2.is_completed()}")
# print(f"Заказ '№{my_order2.order_number}', статус '{my_order2.status}', список заказа: {my_order2.dish_list},"
#       f" Итоговая сумма: {my_order2.total_sum} ")

# Задача: Система управления парковкой
# Создайте класс ParkingLot, который моделирует парковку с ограниченным количеством мест.
# У парковки есть определённые свойства и методы для управления машинами.
# Свойства:
# Количество мест — целое число, задаётся при создании парковки (например, 5 мест).
# Список припаркованных машин — список номеров машин (строки, например, "A123BC", "X456YZ").
# Статус парковки — строка, может быть "открыта" или "закрыта".

# class ParkingLot:
#     def __init__(self, total_places):
#         self.total_places = total_places
#         self.parked_cars = []
#         self.parking_status = "открыта"
#
#     def park_car(self, car_name, car_number):
#         if self.parking_status != "открыта":
#             print("Ошибка: парковка закрыта")
#             return
#         if len(self.parked_cars) >= self.total_places:
#             print("Ошибка: нет свободных мест")
#             return
#         if (car_name, car_number) in self.parked_cars:
#              print(f"Ошибка: машина {car_number} уже на парковке")
#              return
#
#         self.parked_cars.append((car_name, car_number))
#         print(f"Авто '{car_name} - {car_number}' припаркована")
#
#     def remove_car(self, car_number):
#         self.parked_cars = [car for car in self.parked_cars if car_number not in car]
#         print(f"Авто '{car_number}' покинуло парковку")
#
#     def change_status(self):
#         if self.parking_status == "открыта":
#             self.parking_status = "закрыта"
#             print("Парковка", self.parking_status)
#         if self.parking_status == "закрыта":
#             self.parking_status = "открыта"
#
#     def show_free_places(self):
#         return self.total_places - len(self.parked_cars)
#
#     def show_cars(self):
#         print("Список авто на парковке на данный момент:", self.parked_cars)
#
# park = ParkingLot(4)
#
# park.park_car("Lexus", "AX057")
# park.park_car("BMW", "AA055")
# park.remove_car("AX057")
# park.change_status()
# park.park_car("Toyota", "AX047")
# park.change_status()
# park.park_car("Niva", "BB303")
# park.park_car("Niva", "BB303")
#
# print("Свободных мест:", park.show_free_places())
# park.show_cars()


# Задача: Система аренды велосипедов
# Создайте класс BikeRental, который моделирует пункт проката велосипедов.
# У пункта есть определённые свойства и методы для управления велосипедами и арендой.
# Свойства:
# Количество велосипедов — целое число, общее число доступных велосипедов (задаётся при создании).
# Список арендованных велосипедов — словарь, где ключ — имя клиента (строка), а значение — количество
# арендованных им велосипедов (целое число).
# Стоимость аренды за час — число с плавающей точкой, одинаково для всех велосипедов (задаётся при создании, например, 5.0).
# Статус пункта — строка, может быть "открыт" или "закрыт".

# class BikeRental:
#     def __init__(self, total_bikes, price_per_hour):
#         self.total_bikes = total_bikes
#         self.price_per_hour = price_per_hour
#         self.bikes_in_use = {}
#         self.rental_status = "open"
#         self.bikes_count = 0
#
#     def rent_bike(self, client_name, total_rent_time):
#         if self.rental_status != "open":
#             print("Error! Bike rental is close!")
#             return
#         if len(self.bikes_in_use) >= self.total_bikes:
#             print("Error! No free bikes to rent!")
#             return
#
#         total_price = total_rent_time * self.price_per_hour
#         total_price = round(total_price, 2)
#
#         self.bikes_in_use[client_name] = {
#             "Rent time": total_rent_time,
#             "Total price": total_price
#         }
#         self.bikes_count += 1
#         print(f"Client '{client_name}' rented bike for {total_rent_time} hours, total price: {total_price}$")
#
#     def return_bike(self, client_name):
#         if client_name in self.bikes_in_use:
#             del self.bikes_in_use[client_name]
#             self.bikes_count -= 1
#             print(f"Client '{client_name}' returned bike")
#
#     def change_status(self):
#         if self.rental_status == "open":
#             self.rental_status = "close"
#             print(f"Status changed to '{self.rental_status}'")
#         else:
#             self.rental_status = "open"
#             print(f"Status changed to '{self.rental_status}'")
#
#     def get_available_bikes(self):
#         return self.total_bikes - self.bikes_count
#
#
# bike = BikeRental(5, 5.50)
#
# bike.rent_bike("Max", 3)
# bike.rent_bike("Carl", 4)
# bike.rent_bike("Michael", 2.5)
# bike.return_bike("Carl")
#
# print("Available bikes:", bike.get_available_bikes())
# print("Current bikes in use:",bike.bikes_in_use)
#
# bike.change_status()
# bike.change_status()

# Задача: Система управления заказами
# Создай систему управления заказами для интернет-магазина. Тебе нужно реализовать классы для товаров, заказов и покупателей.
# Класс Product (Товар):
# Атрибуты: name (название), price (цена), quantity (количество на складе).
# Метод __str__(), возвращающий строковое представление товара.
# Класс Order (Заказ):
# Атрибуты: products (список товаров в заказе), total_price (общая стоимость заказа).
# Метод add_product(product, quantity), который добавляет товар в заказ, если он есть в наличии.
# Метод remove_product(product), который удаляет товар из заказа.
# Метод checkout(), который уменьшает количество товаров на складе и очищает заказ.
# Класс Customer (Покупатель):
# Атрибуты: name (имя), orders (список заказов).
# Метод place_order(order), который добавляет заказ в список покупателя.

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         return f"Product '{self.name}' with price '{self.price}$' in quantity '{self.quantity}' in storage"
#
# class Order:
#     def __init__(self):
#         self.products = []
#         self.total_price = 0
#
#     def add_product(self, product, quantity):
#         if product.quantity >= quantity:
#             self.products.append((product, quantity))
#             product.quantity -= quantity
#             self.total_price += product.price * quantity
#             print(f"Product '{product.name}' in quantity '{quantity}' added to order!")
#         else:
#             print("Not enough products on storage!")
#
#     def remove_product(self, product):
#         self.products = [prod for prod in self.products if product not in prod]
#         print(f"Product '{product.name}' was deleted")
#
#     def show_order(self):
#         if not self.products:
#             print("No products in order!")
#         else:
#             print("Products in order:")
#         for product, quantity in self.products:
#             print(f"Product '{product.name}' in quantity '{quantity}' in order")
#         print(f"total price {self.total_price}$")
#
#     def __str__(self):
#         if not self.products:
#             return "Order is empty."
#         product_list = [f"{product.name} x {quantity} - {product.price * quantity}$" for product, quantity in self.products]
#         return f"Order:{product_list} Total price: {self.total_price}$"
#
# class Customer:
#     def __init__(self, name):
#         self.name = name
#         self.customer_orders = []
#
#     def create_order(self, order):
#         self.customer_orders.append(order)
#         print(f"Order for '{self.name}' is created!")
#
#     def view_orders(self):
#         for order in self.customer_orders:
#             print(order)
#
#     def __str__(self):
#         return f"Customer {self.name}"
#
#
# milk = Product("Milk", 2.50, 5)
# cake = Product("Cake", 5.50, 3)
# beer = Product("Beer", 3, 7)
# cumstomer1 = Customer("John Wick")
#
# order1 = Order()
# order1.add_product(milk, 4)
# order1.add_product(cake, 1)
# order1.add_product(beer, 2)
# order1.remove_product(cake)
# order1.show_order()
#
# cumstomer1.create_order(order1)
# cumstomer1.view_orders()