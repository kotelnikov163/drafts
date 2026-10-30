def fibonacci(n):
    # Шаг 1. Задаем начальные значения (0 и 1)
    current = 0
    next_num = 1
    
    # Шаг 2. Запускаем цикл, который выполнится n раз
    for _ in range(n):
        # Возвращаем текущее число и "замираем" до следующего запроса
        yield current
        
        # Шаг 3. Вычисляем следующее число
        # Это та строка, которую вы уже написали на 16 строке:
        current, next_num = next_num, current + next_num

# Ниже идет код, который уже был в задании:
sequence = fibonacci(10)
for number in sequence:
    print(number)