class MushroomsCollector:
    
    def __init__(self):
        # Создаем пустой список ВНУТРИ метода, чтобы у каждого 
        # сборщика была своя независимая корзина (а не общая на всех).
        self.mushrooms = []

    def is_poisonous(self, mushroom_name):
        # Сравниваем имя с каждым вариантом отдельно через 'or'.
        # (Запись `== 'Мухомор' or 'Поганка'` — не сработает, т.к. непустая строка всегда True).
        if mushroom_name == 'Мухомор' or mushroom_name == 'Поганка':
            return True
        return False

    def add_mushroom(self, mushroom_name):
        # Если метод is_poisonous вернул False, значит гриб съедобный (not False = True).
        if not self.is_poisonous(mushroom_name):
            # Добавляем в личную корзину, используя переданный аргумент (без self.).
            self.mushrooms.append(mushroom_name)
        else:
            print('Нельзя добавить ядовитый гриб')

    def __str__(self):
        # Метод join склеивает элементы списка в строку через ', '.
        # Это убирает квадратные скобки и кавычки при выводе через print().
        return ', '.join(self.mushrooms)