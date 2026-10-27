# ==========================================
# Базовый класс сотрудника
# ==========================================
class Employee:
    # Атрибут класса: фиксированное количество дней отпуска по умолчанию
    vacation_days = 28

    def __init__(self, first_name, last_name, gender):
        # Сохраняем базовые данные сотрудника
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        
        # Изначально количество оставшихся дней равно стандартному отпуску
        self.remaining_vacation_days = self.vacation_days
        
        # Вызываем приватный метод для генерации ID и сохраняем в защищенный атрибут
        self._employee_id = self.__generate_employee_id()

    # Приватный метод (начинается с __) для генерации уникального ID
    def __generate_employee_id(self):
        # Склеиваем имя, фамилию и пол в одну строку без пробелов
        concat_string = f'{self.first_name}{self.last_name}{self.gender}'
        # Превращаем полученную строку в уникальное число с помощью встроенной функции hash()
        return hash(concat_string)

    # Метод для списания дней отпуска
    def consume_vacation(self, days):
        # Уменьшаем счетчик оставшихся дней на запрошенное количество
        self.remaining_vacation_days -= days

    # Метод для получения текущего остатка дней отпуска
    def get_remaining_vacation_days(self):
        return self.remaining_vacation_days


# ==========================================
# Класс офисного сотрудника (наследуется от Employee)
# ==========================================
class OfficeEmployee(Employee):
    def __init__(self, first_name, last_name, gender, worker_class, salary):
        # Вызываем конструктор родительского класса, чтобы он задал имя, фамилию, пол и 28 дней отпуска
        super().__init__(first_name, last_name, gender)
        
        # Добавляем новые атрибуты, свойственные только офисным сотрудникам
        self.worker_class = worker_class
        self.__salary = salary  # Приватный атрибут (два подчеркивания) для зарплаты
        
        # Увеличиваем отпуск на дополнительные дни в зависимости от разряда (по 2 дня за каждый разряд)
        self.remaining_vacation_days += self.worker_class * 2

    # Метод для расчета отпускных выплат
    def get_vacation_payment(self, days):
        # Стоимость одного дня отпуска — это 1/60 от зарплаты
        # Умножаем стоимость одного дня на количество запрошенных дней
        payment = (self.__salary / 60) * days
        
        # По условию результат нужно привести к целому числу (отбрасываем дробную часть)
        return int(payment)


# ==========================================
# Блок проверки работы кода
# ==========================================
# Создаем экземпляр офисного сотрудника
office_employee = OfficeEmployee(
    first_name='Иван',
    last_name='Иванов',
    gender='м',
    worker_class=2,
    salary=45000
)

# Допустим, сотрудник хочет взять 10 дней отпуска
vacation_days = 10

# Списываем эти дни
office_employee.consume_vacation(vacation_days)

# Выводим остаток дней (ожидается 22: было 28 + 4 доп. = 32, минус 10 = 22)
print(f'У сотрудника осталось {office_employee.get_remaining_vacation_days()} дн. отпуска.')

# Выводим сумму отпускных (45000 / 60 * 10 = 7500)
print(f'За {vacation_days} дн. отпуска сотрудник получит {office_employee.get_vacation_payment(vacation_days)} руб.')