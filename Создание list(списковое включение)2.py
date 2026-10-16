# Исходный список урожайности (кг на дерево)
fruit_yields = [164.8, 105.0, 124.3, 113.8]

# Списковое включение: создаём новый список,
# где к каждому значению прибавляем 1.2
corrected_fruit_yields = [yield_value + 1.2 for yield_value in fruit_yields]

# Выводим скорректированный список на экран
print(corrected_fruit_yields)