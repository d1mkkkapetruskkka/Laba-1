# Функция для определения, является ли символ гласной буквой
def is_vowel(char):
    vowels = "AEIOUaeiou"
    return char in vowels

# Ввод текста с клавиатуры
text = input("Введите текст: ")

# Инициализируем счетчики для гласных и согласных
vowel_count = 0
consonant_count = 0

# Список для хранения гласных букв
vowels_list = []

# Перебираем символы в тексте
for char_input in text:
    if char_input.isalpha():  # Проверяем, является ли символ буквой
        if is_vowel(char_input):
            vowel_count += 1
            vowels_list.append(char_input)
        else:
            consonant_count += 1

# Выводим результат
print("Количество гласных букв:", vowel_count)
print("Количество согласных букв:", consonant_count)

if vowel_count == consonant_count:
    print("Гласные буквы в тексте:", ", ".join(vowels_list))
