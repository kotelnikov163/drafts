# Декоратор принимает функцию (метод), которую нужно обернуть
def validate_fuel_consumption(method):
    """
    Декоратор для проверки условий перед расчётом расхода топлива.
    Проверяет, что время или расстояние неотрицательны и достаточно топлива.
    """
    # wrapper — это новая функция, которая заменит оригинальный метод
    def wrapper(self, value):
        # 1. Проверяем входное значение (расстояние или время) на отрицательность
        if value < 0:
            print("Ошибка: значение не может быть отрицательным.")
            return None  # Прерываем выполнение, если данные некорректны
            
        # 2. Вызываем оригинальный метод (он посчитает нужное количество топлива)
        consumption = method(self, value)
        
        # 3. Если оригинальный метод по какой-то причине вернул None — прерываемся
        if consumption is None:
            return None
            
        # 4. Проверяем, хватает ли топлива в баке для такой поездки/полета
        if consumption > self._current_fuel_level:
            # Используем :.2f для красивого вывода (округление до 2 знаков)
            print(f"Ошибка: недостаточно топлива для поездки. Нужно {consumption:.2f} л., в наличии {self._current_fuel_level:.2f} л.")
            return None
            
        # 5. Если все проверки пройдены — списываем потраченное топливо из бака
        self._current_fuel_level -= consumption
        return consumption
        
    return wrapper  # Возвращаем обернутую функцию


class Vehicle:
    """
    Базовый класс для транспортных средств.
    """
    def __init__(self, name, fuel_tank_capacity):
        # Атрибуты с нижним подчеркиванием считаются защищенными (по ТЗ)
        self._name = name
        self._fuel_tank_capacity = fuel_tank_capacity
        # При создании объекта бак всегда полный
        self._current_fuel_level = fuel_tank_capacity

    def refuel(self, amount):
        """
        Заправка транспортного средства.
        """
        # Проверка: нельзя залить отрицательное или нулевое количество топлива
        if amount <= 0:
            print("Ошибка: количество топлива должно быть положительным.")
            return
            
        # Проверка: не переполнится ли бак при заправке
        if self._current_fuel_level + amount > self._fuel_tank_capacity:
            print("Ошибка: превышение вместимости топливного бака.")
            return
            
        # Если проверки пройдены — увеличиваем уровень топлива
        self._current_fuel_level += amount
        print(f"Заправлено {amount} л. Текущий уровень: {self._current_fuel_level} л.")

    def display_info(self):
        """
        Отображает основную информацию о транспортном средстве.
        """
        # Выводим данные, подставляя значения защищенных атрибутов
        print(f"Название: {self._name}, Вместимость бака: {self._fuel_tank_capacity} л, Текущий уровень топлива: {self._current_fuel_level} л.")


class Car(Vehicle):
    """
    Класс для представления автомобиля.
    Наследует от Vehicle.
    """
    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_100km):
        # Вызываем конструктор родителя, чтобы инициализировать имя и бак
        super().__init__(name, fuel_tank_capacity)
        # Дополнительный атрибут только для машины — расход на 100 км
        self._fuel_consumption_per_100km = fuel_consumption_per_100km

    # Применяем наш декоратор к методу расчета
    @validate_fuel_consumption
    def calculate_fuel_consumption(self, distance):
        # Формула расхода для авто: (км / 100) * расход_на_100_км
        consumption = (distance / 100) * self._fuel_consumption_per_100km
        print(f"Расход на {distance} км: {consumption:.2f} л.")
        return consumption


class Airplane(Vehicle):
    """
    Класс для представления самолёта.
    Наследует от Vehicle.
    """
    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_hour):
        super().__init__(name, fuel_tank_capacity)
        # У самолета расход считается за час полета
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, hours):
        # Формула расхода для самолета: время * расход_в_час
        consumption = hours * self._fuel_consumption_per_hour
        print(f"Расход за {hours} ч: {consumption:.2f} л.")
        return consumption


class Boat(Vehicle):
    """
    Класс для представления катера.
    Наследует от Vehicle.
    """
    def __init__(self, name, fuel_tank_capacity, fuel_consumption_per_hour):
        super().__init__(name, fuel_tank_capacity)
        # У катера, как и у самолета, расход считается за час
        self._fuel_consumption_per_hour = fuel_consumption_per_hour

    @validate_fuel_consumption
    def calculate_fuel_consumption(self, hours):
        # Формула расхода для катера: время * расход_в_час
        consumption = hours * self._fuel_consumption_per_hour
        print(f"Расход за {hours} ч: {consumption:.2f} л.")
        return consumption


# ==========================================
# Блок тестирования (демонстрация работы)
# ==========================================

# Создаем объекты (бак сразу заполняется до краев)
car = Car("Toyota Camry", 60, 8)
airplane = Airplane("Boeing 737", 20000, 2500)
boat = Boat("Sea Ray", 150, 30)

# Выводим базовую информацию о каждом ТС
car.display_info()
airplane.display_info()
boat.display_info()

# Пытаемся заправить (ожидаем ошибки, т.к. баки изначально полные)
car.refuel(30)
airplane.refuel(10000)
boat.refuel(80)

# Считаем расход (декоратор проверит данные и спишет топливо)
car.calculate_fuel_consumption(150)
airplane.calculate_fuel_consumption(3)
boat.calculate_fuel_consumption(2)