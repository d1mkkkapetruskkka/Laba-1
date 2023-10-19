# Исходный список
list = [1, 34, 'qwerty', 12, 13, 16, 'Love', 'Python']
# Создаем отдельный список из слов и чисел
words_list = [item for item in list if isinstance(item, str)]
numbers_list = [item for item in list if isinstance(item, int)]

# Вычисляем сумму и произведение чисел
sum_of_numbers = sum(numbers_list)
product_of_numbers = 1
for num in numbers_list:
    product_of_numbers *= num

# Выводим результаты
print("Список слов:", words_list)
print("Список чисел:", numbers_list)
print("Сумма чисел:", sum_of_numbers)
print("Произведение чисел:", product_of_numbers)

# Выводим три наибольших элемента из числового списка
if len(numbers_list) >= 3:
    largest_numbers = sorted(numbers_list, reverse=True)[:3]
    print("Три наибольших элемента:", largest_numbers)
else:
    print("В числовом списке нет трех элементов.")
