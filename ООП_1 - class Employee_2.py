class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        
        self.remaining_vacation_days = self.vacation_days
    
    def consume_vacation(self, days):
        self.remaining_vacation_days = self.remaining_vacation_days - days
        
    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'
    
    def __str__(self):
        return f'Сотрудник: {self.first_name} {self.second_name}, Пол: {self.gender}, остаток отпуска: {self.remaining_vacation_days} дней.'

employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)
print(employee.get_vacation_details())
