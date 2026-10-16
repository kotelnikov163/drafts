def print_pack_report(starting_value):
    # Диапазон от starting_value до 1 включительно, в обратном порядке
    for number in range(starting_value, 0, -1):
        if number % 3 == 0 and number % 5 == 0:
            print(f'{number} - расфасуем по 3 или по 5')
        elif number % 3 != 0 and number % 5 == 0:
            print(f'{number} - расфасуем по 5')
        elif number % 3 == 0 and number % 5 != 0:
            print(f'{number} - расфасуем по 3')
        else:
            print(f'{number} - не заказываем!')

print_pack_report(31)