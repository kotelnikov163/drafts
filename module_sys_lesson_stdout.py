import sys

# Сохраняем оригинальный поток вывода
original_stdout = sys.stdout

# Открываем файл для записи
log_file = open("заказы.log", "w", encoding="utf-8")

# Перенаправляем вывод в файл
sys.stdout = log_file

# Теперь все print() будут писать в файл, а не на экран
print("Заказ № 1: Пицца, 500 руб.")
print("Заказ № 2: Суши, 800 руб.")
print("Заказ № 3: Бургер, 350 руб.")

# Возвращаем вывод обратно на экран
sys.stdout = original_stdout
log_file.close()

print("Лог заказов сохранён в файл!")  # Это уже на экран