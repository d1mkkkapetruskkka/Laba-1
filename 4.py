# Исходная строка
text = 'An apple a day keeps the doctor away'

# Инициализируем пустой словарь
char_count = {}

# Перебираем символы в строке
for char in text:
    # Игнорируем пробелы
    if char != ' ':
        # Если символ уже есть в словаре, увеличиваем счетчик
        if char in char_count:
            char_count[char] += 1
        # Если символа нет в словаре, добавляем его и устанавливаем счетчик в 1
        else:
            char_count[char] = 1

# Выводим получившийся словарь
print(char_count)
