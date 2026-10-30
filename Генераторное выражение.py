 # Список для тестирования
numbers = [1, 3, 4, 6, 9, 11]

# Генераторное выражение и подсчет суммы
sum_of_squares = sum(x**2 for x in numbers if x % 3 == 0)

print(sum_of_squares)