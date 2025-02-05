# #
# 1 Задача:
# # Напиши программу, которая принимает список чисел и выводит максимальное четное число в этом списке.
# # Если четных чисел нет, программа должна вывести сообщение "Нет четных чисел".
#
# # Введите числа через пробел: 3 7 2 8 1
# # Максимальное четное число: 8
# #
# # Введите числа через пробел: 3 7 1
# # Нет четных чисел
# numbers = []
# numbers = input("Enter your number by Space: ").split(" ")
# numbers = [int(num) for num in numbers]
# even_numbers = [num for num in numbers if num % 2 == 0]
# print("Your max. number is: ", max(numbers))
import re
from os import remove

# 2 Напиши программу, которая принимает от пользователя строку и выводит самое длинное слово в этой строке.
# # Если таких слов несколько, программа должна вывести первое из них.
#
# # Введите строку: Я изучаю программирование на Python
# # Самое длинное слово: программирование
# # Введите строку: Кот спит на окне
# # Самое длинное слово: окно
#
# user_text = input("Enter your text: ")
# words = user_text.split()
# langest_word = max(words, key=len)
# print("Your langest word is: ", langest_word)

# 3 Напиши программу, которая принимает целое число от пользователя и проверяет, является ли оно палиндромом (читается одинаково слева направо и справа налево).
# #
# # Введите число: 12321
# # Число является палиндромом.
# #
# # Введите число: 12345
# # Число не является палиндромом.
#
# user_number = input("Enter your number: ")
# if user_number == user_number[::-1]:
#     print("This is palindrome!")
# else:
#     print("This is not palindrome")


#4 Напиши программу, которая принимает от пользователя возраст и выводит, к какой категории он относится:
#
# 0–12 лет → Ребенок
# 13–17 лет → Подросток
# 18–64 года → Взрослый
# 65 и старше → Пенсионер
# Меньше 0 → Ошибка
#
# user_age = int(input("Enter your age: "))
# if user_age < 0:
#     print("Error")
# elif 0 <= user_age <= 12:
#     print("You are a child!")
# elif 13 <= user_age <= 17:
#     print("You are a teenager!")
# elif 18 <= user_age <= 64:
#     print("You are a adult")
# else:
#     print("You are old")

#5 Напиши программу, которая проверяет, является ли введенное число четным или нечетным и положительным или отрицательным.
# Если число равно нулю, программа должна вывести "Число равно 0".

# user_number = int(input("Enter your number: "))
# if user_number == 0:
#     print(f"Your number:{user_number} is 0")
# elif 0 < user_number:
#     print(f"Your number:{user_number} is positive")
# elif 0 > user_number:
#     print(f"Your number:{user_number} is negative")
# if user_number % 2 == 0:
#     print(f"Your number:{user_number} is even")
# else:
#     print(f"You number:{user_number} is odd")

# 6
# Напиши программу, которая принимает от пользователя три стороны и проверяет, можно ли из них составить треугольник.
# 📌 Условие существования треугольника:
# Сумма любых двух сторон должна быть больше третьей.
# То есть, если стороны a, b, c, то должно выполняться:
# a + b > c
# a + c > b
# b + c > a

# user_value1 = int(input("Enter 1 value for triangle: "))
# user_value2 = int(input("Enter 2 value for triangle: "))
# user_value3 = int(input("Enter 3 value for triangle: "))
# if (user_value1 + user_value2 > user_value3 and
#         user_value1 + user_value3 > user_value2 and
#         user_value2 + user_value3 > user_value1):
#     print("This is triangle!")
# else:
#     print("This is not triangle!")

#7 Напиши программу, которая принимает список чисел от пользователя, а затем:
# Находит сумму всех чисел.
# Находит максимальное и минимальное число.
# Создает отдельный список только из четных чисел.
# Пример работы:

# Введите числа через пробел: 4 7 1 8 3 10
# Сумма всех чисел: 33
# Максимальное число: 10
# Минимальное число: 1
# Четные числа: [4, 8, 10]

# user_numbers = [int(num) for num in input("Enter your numbers: ").split(" ")]
# numbers_sum = sum(user_numbers)
# max_min_numbers = max(user_numbers), min(user_numbers)
# even_numbers = [num for num in user_numbers if num % 2 == 0]
# print(f"All numbers sum: {numbers_sum}, max/min value: {max_min_numbers}, your even numbers: {even_numbers}")

#8 Напиши программу, которая:
#
# Принимает от пользователя список чисел.
# Сортирует список по возрастанию.
# Создает новый список, который будет содержать только уникальные числа из этого списка.
# Выводит отсортированный список и новый список с уникальными числами.
# Пример работы:

# Введите числа через пробел: 3 5 2 3 8 5 2 1 9
# Отсортированный список: [1, 2, 2, 3, 3, 5, 5, 8, 9]
# Список уникальных чисел: [1, 2, 3, 5, 8, 9]
#
# user_numbers = [int(num) for num in input("Enter your numbers with <Space>: ").split(" ")]
# user_numbers.sort()
# unique_numbers = sorted(set(user_numbers))
# print(f"Your numbers: {user_numbers}, unique numbers: {unique_numbers}")

#9 Напиши программу, которая:
#
# Принимает от пользователя список чисел.
# Создает новый список, в котором будут только положительные числа из оригинального списка, но умноженные на 2.
# Выводит новый список.

# Введите числа через пробел: -1 2 -3 4 5 -6
# Новый список: [4, 8, 10]

# user_numbers = [int(num) for num in input("Enter your numbers: ").split()]
# multiply_numbers = [num * 2 for num in user_numbers]
# print(f"Your multiply values: {multiply_numbers}")

#10 Задача: Калькулятор чаевых
# Напиши программу, которая спрашивает у пользователя:
# Общую сумму счёта в ресторане
# Процент чаевых, который он хочет оставить
# Количество человек, на которых нужно разделить счёт
# Программа должна:
#
# Рассчитать сумму чаевых.
# Добавить её к общей сумме счёта.
# Разделить сумму на количество человек.
# Вывести сумму, которую должен заплатить каждый.

# Введите сумму счёта: 100
# Введите процент чаевых: 10
# Введите количество человек: 2
# Каждый должен заплатить: 55.0

# order_sum = int(input("Enter your order price: "))
# tips_percent = int(input("How many tips in % you want to give?: "))
# guests = int(input("How many guests were served?: "))
# if tips_percent >= 0 and order_sum > 0 and guests > 0:
#     tips = order_sum * tips_percent / 100
#     total_sum = order_sum + tips
#     print(f"Total price for each guest: {total_sum / guests:.1f}")

# 11 Задача: Проверка пароля
# Напиши программу, которая:
#
# Запрашивает у пользователя пароль.
# Проверяет, соответствует ли он следующим требованиям:
# Длина от 8 до 16 символов.
# Содержит хотя бы одну цифру.
# Содержит хотя бы одну заглавную букву.
# Содержит хотя бы одну строчную букву.
# Выводит сообщение, соответствует ли пароль требованиям.

# Примеры работы:
# pgsql
# Enter a password: qwerty
# Password is too weak!
# pgsql
# Enter a password: Qwerty123
# Password is strong! ✅

# user_pass = input("Create your password: ")
# pass_lenth = len(user_pass)
# if pass_lenth < 8 or pass_lenth > 16 or user_pass.strip() =="":
#     print("Invalid password")
# if re.search(r"[0-9]", user_pass):
#     print("Your password contains at least 1 number")                                                           #number
# else:
#     print(print("Your password contains not any number"))
# if re.search(r"[A-Z]", user_pass):
#     print("Your pass contains at least 1 big letter")                                                           #Bletter
# else:
#     print(print("Your pass contains not any big letter"))
# if re.search(r"[a-z]", user_pass):
#     print("Your pass contains at least 1 small letter")                                                         #Sletter
# else:
#     print(print("Your pass contains not any small letter"))

# 12 Задача: Игра "Угадай число" 🎲
# Условие:
#
# Программа загадывает случайное число от 1 до 100.
# Пользователь пытается угадать число.
# Программа даёт подсказки:
# Если число меньше загаданного → "Больше!"
# Если число больше загаданного → "Меньше!"
# Если число угадано → "Поздравляю, ты угадал число!"
# Игра продолжается, пока пользователь не угадает число.

# key_number = 73
# while True:
#     user_number = int(input("Guess the number (1-100): "))
#     if user_number >= 100 or user_number <= 0:
#         print("Invalid number!")
#     elif user_number == key_number:
#         print("You win! Its correct number")
#         break
#     elif user_number < key_number:
#         print("More!")
#     elif user_number > key_number:
#         print("Less!")
#
#13 3адача: Система учёта сотрудников в компании 👩‍💻👨‍💻
# Условие:
# Необходимо создать простую систему для учёта сотрудников компании, которая будет:

# Позволять добавлять информацию о сотрудниках.
# Сохранять их в список.
# Позволять искать сотрудников по имени.
# Выводить информацию о всех сотрудниках.

# Функциональность программы:
# Добавление сотрудника (имя, должность, возраст).
# Поиск сотрудника по имени.
# Вывод всех сотрудников.
# comp_workers = [["Ivanov", "Developer", 28], ["Petrov", "Team lead", 50], ["Sydorov", "Fixer", 20],
#                 ["Koval", "Cleaner", 35]]
#
# while True:
#
#     print("\nСистема учёта сотрудников в компании")
#     print("1. Вывод списка сотрудников")
#     print("2. Найти сотрудника по имени")
#     print("3. Добавить сотрудника")
#     print("4. Удалить сотрудника")
#     print("5. Выход с системы")
#
#     case = input("Введите номер опции(1-4): ")
#
#
#     match case:
#         case "1":
#             if comp_workers:
#                 print("\n Список сотрудников:")
#             for worker in comp_workers:
#                 print(f"Имя сотрудника: {worker[0]}, Должность: {worker[1]}, Возраст: {worker[2]}")
#
#
#         case "2":
#             search_name = input("Введите имя сотрудника: ")
#             found = False
#             for worker in comp_workers:
#                 if worker[0].lower() == search_name.lower():
#                     print(f"Найден сотрудник: {worker[0]} - {worker[1]} - {worker[2]}")
#                     found = True
#                 if not found:
#                     print("Сотрудник не найден")
#
#                 break
#
#         case "3":
#             add_worker = input("Впишите через запятую Фамилию, Должность, Возраст нового сотрудника: ").split(", ")
#             if len(add_worker) == 3:
#                 try:
#                     add_worker[2] = int(add_worker[2])
#                     comp_workers.append(add_worker)
#                     print(f"Новый сотрудник {add_worker} успешно внесен в базу!")
#                 except ValueError:
#                     print("Ошибка! Возраст должен быть числом")
#
#         case "4":
#             delete_worker = input("Введите фамилию сотрудника для удаления: ")
#             delete = False
#             for worker in comp_workers:
#                 if worker[0].lower() == delete_worker.lower():
#                     comp_workers.remove(worker)
#                     print(f"Указанный сотрудник {delete_worker} удален с БД")
#                     delete = True
#                     break
#                 if not delete:
#                     print("Сотрудник не найден!")
#
#         case "5":
#             print("Сеанс завершен!")
#             break


# 14 📌 Напишите функцию multiply_numbers(a, b), которая принимает два числа и возвращает их произведение.
#
# Примеры работы функции:
# print(multiply_numbers(4, 5))   # 20
# print(multiply_numbers(-3, 6))  # -18
# print(multiply_numbers(0, 10))  # 0
# numbers = ((4,5), )
#
# def multiply_numbers(a, b):
#     return a * b
# print(multiply_numbers(4, 5))   # 20
# print(multiply_numbers(-3, 6))  # -18
# print(multiply_numbers(0, 10))  # 0

#15 📌 Напишите функцию is_even(number), которая принимает число и возвращает True, если оно чётное, и False, если нечётное.

# def is_even(number):
#     return number % 2 == 0
#
#
# print(is_even(4))   # True
# print(is_even(7))   # False
# print(is_even(0))   # True

# 15 📌 Напишите функцию count_vowels(text), которая принимает строку и возвращает количество гласных букв в этой строке.
# Гласные: a, e, i, o, u (в нижнем и верхнем регистре).

# def count_vowels(text):
#     count_vowels = 0
#     vowels = "aeiouAEIOU"
#     for sym in text:
#         if sym in vowels:
#             count_vowels += 1
#
#     return  count_vowels
#
# print(count_vowels("Hello World"))   # 3
# print(count_vowels("Python"))        # 1
# print(count_vowels("AEIOUaeiou"))    # 10

# 📌 Напишите функцию count_numbers(text), которая принимает строку и возвращает количество чисел в ней.
# Числом считается последовательность цифр (например, "123", "456"). Если в строке есть символы, не являющиеся цифрами, они должны быть проигнорированы.
# def count_numbers(text):
#     count_num = 0
#     words = text.split()
#     for word in words:
#         if word.isdigit():
#             count_num += 1
#
#     return count_num
#
# print(count_numbers("I have 2 apples and 3 bananas"))   # 2
# print(count_numbers("There are 4 dogs and 1 cat"))      # 2
# print(count_numbers("No numbers here!"))                # 0


# Задача: Перевод температуры
# 📌 Напишите функцию convert_temperature(temp, scale), которая принимает температуру temp и шкалу scale
# ("C" для Цельсия или "F" для Фаренгейта). Функция должна возвращать температуру в другой шкале.
# Если входная температура дана в Цельсиях, функция должна перевести её в Фаренгейты.
# Если входная температура дана в Фаренгейтах, функция должна перевести её в Цельсиях.
# Формулы для перевода:
# Цельсий в Фаренгейт: (temp * 9/5) + 32
# Фаренгейт в Цельсий: (temp - 32) * 5/9

# def convert_temperature(temp, scale):
#     if scale == "C":
#         convert = (temp * 9/5) + 32
#     elif scale == "F":
#         convert = (temp - 32) * 5/9
#     else:
#         "Invalid scale"
#     return convert
#
#
# print(convert_temperature(100, "C"))  # 212.0
# print(convert_temperature(32, "F"))   # 0.0
# print(convert_temperature(0, "C"))    # 32.0
#
#
# Задача: Обратный порядок слов
# 📌 Напишите функцию reverse_words(text), которая принимает строку и возвращает строку, в которой все слова идут в обратном порядке.
#
# Примечание: слово — это последовательность символов, разделённая пробелами. Нужно перевернуть только порядок слов, а не их содержимое.

# def reverse_words(text):
#     words = text.split()
#     for word in words:
#         reversed_word = word[1:1]
#     return reversed_word
#
# print(reverse_words("Hello World"))      # "World Hello"
# print(reverse_words("Python is awesome"))  # "awesome is Python"
# print(reverse_words("I love coding"))      # "coding love I"


# Задача:
# Напиши функцию make_multiplier(factor), которая принимает число factor и возвращает функцию, умножающую переданный ей аргумент на этот factor.

# def make_multiplier(factor):
#     def multi(num):
#         return num * factor
#     return multi
#
# double = make_multiplier(2)
# triple = make_multiplier(3)
# print(double(5))  # Вывод: 10
# print(triple(4))  # Вывод: 12

# Напиши функцию make_power(exponent), которая принимает степень exponent и возвращает функцию, возводящую переданное число в эту степень.
# def make_power(exponent):
#     def power(num):
#         return num ** exponent
#     return power
#
# square = make_power(2)
# cube = make_power(3)
# print(square(4))  # Вывод: 16 (4^2)
# print(cube(2))    # Вывод: 8 (2^3)

