import random

# Функция для создания случайного кортежа
def generate_random_tuple():
    length = random.randint(1, 10)  # Генерируем случайную длину кортежа от 1 до 10 элементов
    random_tuple = tuple(random.randint(1, 100) for _ in range(length))  # Заполняем кортеж случайными числами
    return random_tuple

# Функция для ввода кортежа вручную
def input_manual_tuple():
    input_str = input("Введите элементы кортежа через пробел: ")
    elements = input_str.split()
    try:
        manual_tuple = tuple(map(int, elements))
        return manual_tuple
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числа через пробел.")
        return None

# Функция для нахождения наименьшего четного элемента в кортеже
def find_min_even_element(my_tuple):
    min_even = None
    for item in my_tuple:
        if item % 2 == 0:
            if min_even is None or item < min_even:
                min_even = item
    return min_even

# Выбор способа ввода кортежа
while True:
    print("Выберите способ ввода кортежа:")
    print("1. Ввести кортеж вручную")
    print("2. Сгенерировать случайный кортеж")
    print("3. Выйти")

    choice = input("Ваш выбор: ")

    if choice == '1':
        manual_tuple = input_manual_tuple()
        if manual_tuple is not None:
            min_even = find_min_even_element(manual_tuple)
            if min_even is not None:
                print(f"Наименьший четный элемент: {min_even}")
            else:
                print(f"Наименьший четный элемент не найден. Первый элемент кортежа: {manual_tuple[0]}")
    elif choice == '2':
        random_tuple = generate_random_tuple()
        print(f"Случайный кортеж: {random_tuple}")
        min_even = find_min_even_element(random_tuple)
        if min_even is not None:
            print(f"Наименьший четный элемент: {min_even}")
        else:
            print(f"Наименьший четный элемент не найден. Первый элемент кортежа: {random_tuple[0]}")
    elif choice == '3':
        print("Выход из программы.")
        break
    else:
        print("Пожалуйста, выберите корректный пункт меню.")