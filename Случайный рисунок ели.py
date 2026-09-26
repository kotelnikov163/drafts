import random

def draw_tree(height):
    width = 2 * height - 1  # Вычисляем ширину основания кроны.
    for i in range(height):
        stars = 2 * i + 1  # Количество звездочек на текущем уровне кроны.
        spaces = (width - stars) // 2  # Количество пробелов для выравнивания по центру.
        print(' ' * spaces + '*' * stars)  # Печатаем текущий уровень кроны.

def draw_trunk(height):
    trunk_width = random.choice([1, 3])  # Определяем случайную ширину ствола.
    trunk_height = height // 4  # Определяем высоту ствола в зависимости от высоты кроны.
    trunk_space = (2 * height - 1 - trunk_width) // 2  # Выравниваем ствол по центру кроны.
    for _ in range(trunk_height):
        print(' ' * trunk_space + '|' * trunk_width)  # Печатаем текущий уровень ствола.


tree_height = random.randint(5, 15)  # Генерируем случайную высоту дерева.
draw_tree(tree_height)   # Вычисляем и печатаем крону.
draw_trunk(tree_height)  # Вычисляем и печатаем ствол.