# Задача: Система учета студентов
# Создайте класс Student, который будет хранить информацию о студенте и его оценках. Реализуйте следующие возможности:
# Хранение имени, возраста и списка оценок студента.
# Метод для добавления новой оценки.
# Метод для вычисления среднего балла.
# Метод для определения, является ли студент отличником (средний балл >= 4.5).



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



