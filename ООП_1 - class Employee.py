class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def go_to_work(self):
        print(f'{self.name} вышел на работу')

    def raise_salary(self, amount):
        self.salary += amount
        print(f'{self.name} повышен. Новая зарплата: {self.salary}')

    def get_yearly_salary(self):
        return self.salary * 12

    def __str__(self):
        return f'Сотрудник: {self.name}, должность: {self.position}, зарплата: {self.salary}'


emp1 = Employee('Максим', 'Автор', 90000)
print(emp1) # Сотрудник: Максим, должность: Автор, зарплата: 90000
