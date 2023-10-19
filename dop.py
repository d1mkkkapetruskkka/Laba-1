# Введите строку с клавиатуры
input_string = input("Введите строку: ")

# Разделяем строку на символы
characters = list(input_string)

# Инициализируем переменные для формирования числа
current_number = ''
numbers = []

# Перебираем каждый символ в строке
for char in characters:
    if char.isdigit():  # Если символ - цифра, добавляем его к текущему числу
        current_number += char
    elif current_number:  # Если текущее число не пустое, добавляем его в список чисел
        numbers.append(int(current_number))
        current_number = ''# Сбрасываем текущее число

# Если последний символ в строке был числом, добавляем его
if current_number:
    numbers.append(int(current_number))

# Выводим найденные числа
for number in numbers:
    print(number)