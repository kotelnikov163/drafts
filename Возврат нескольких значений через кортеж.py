def bizarre_function(first, second, third):
    total = first + second + third
    multiplication = first * second * third
    string = str(first) + str(second) + str(third)
    # Перечисление значений через запятую - это способ объявить кортеж!
    return total, multiplication, string

result = bizarre_function(2, 4, 6)  # Вызываем функцию, результат присваиваем
                                    # переменной result. Результат - это кортеж.

a, b, c = result  # Распаковываем кортеж в переменные a, b и c.

print('Сумма значений 2, 4 и 6:', a)
print('Произведение значений 2, 4 и 6:', b)
print('Строка, составленная из значений 2, 4 и 6:', c)

print('\_(ツ)_/¯')

# Распаковать можно и без применения промежуточной переменной result:
d, e, f = bizarre_function(3, 5, 7)  # Вызов и распаковка - одной строкой.

print('Сумма значений 3, 5 и 7:', d)
print('Произведение значений 3, 5 и 7:', e)
print('Строка, составленная из значений 3, 5 и 7:', f)