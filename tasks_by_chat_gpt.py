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