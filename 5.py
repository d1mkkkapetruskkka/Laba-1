# Создаем список продуктов с информацией
products = [
    ['Масло', 'Моторное масло для автомобилей', 30.0, 50],
    ['Фильтр масляный', 'Фильтр для масла', 10.0, 100],
    ['Тормозные колодки', 'Тормозные колодки для автомобилей', 20.0, 30],
    ['Свечи зажигания', 'Свечи зажигания для двигателя', 5.0, 80],
    ['Аккумулятор', 'Автомобильный аккумулятор', 50.0, 20],
]

while True:
    # Выводим меню
    print("\nМеню:")
    print("1. Просмотр названия и описания")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Вся информация")
    print("5. Покупка")
    print("6. До свидания")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        for i, product_info in enumerate(products, start=1):
            print(f"{i}. {product_info[0]} - {product_info[1]}")
        product_number = int(input("Выберите номер продукции: ")) - 1
        if 0 <= product_number < len(products):
            print(f"Название: {products[product_number][0]}")
            print(f"Описание: {products[product_number][1]}")
        else:
            print("Продукция не найдена.")

    elif choice == '2':
        for i, product_info in enumerate(products, start=1):
            print(f"{i}. {product_info[0]} - Цена: {product_info[2]}")
        product_number = int(input("Выберите номер продукции: ")) - 1
        if 0 <= product_number < len(products):
            print(f"Цена: {products[product_number][2]}")
        else:
            print("Продукция не найдена.")

    elif choice == '3':
        for i, product_info in enumerate(products, start=1):
            print(f"{i}. {product_info[0]} - Количество: {product_info[3]}")
        product_number = int(input("Выберите номер продукции: ")) - 1
        if 0 <= product_number < len(products):
            print(f"Количество: {products[product_number][3]}")
        else:
            print("Продукция не найдена.")

    elif choice == '4':
        for i, product_info in enumerate(products, start=1):
            print(f"{i}. {product_info[0]} - {product_info[1]}, Цена: {product_info[2]}, Количество: {product_info[3]}")

    elif choice == '5':
        total_price = 0.0
        while True:
            for i, product_info in enumerate(products, start=1):
                print(f"{i}. {product_info[0]} - {product_info[1]}, Цена: {product_info[2]}, Количество: {product_info[3]}")
            product_number = int(input("Выберите номер продукции (или '0' для выхода из покупки): ")) - 1
            if product_number == -1:
                break
            if 0 <= product_number < len(products):
                quantity = int(input("Введите количество: "))
                if quantity > products[product_number][3]:
                    print("Извините, недостаточно товара на складе.")
                else:
                    products[product_number][3] -= quantity
                    total_price += quantity * products[product_number][2]
            else:
                print("Продукция не найдена.")
        print(f"Общая стоимость покупки: {total_price}")

    elif choice == '6':
        print("До свидания!")
        break

    else:
        print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")
