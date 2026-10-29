from datetime import datetime

DATE_FORMAT = '%d.%m.%Y'

def validate_record(name: str, birthdate: str) -> bool:
    try:
        # Пытаемся превратить строку в дату. Если получилось — дата верная.
        datetime.strptime(birthdate, DATE_FORMAT)
        return True
    except ValueError:
        # Если формат неверный, выводим ошибку и возвращаем False.
        print(f'Некорректный формат даты в записи: {name}, {birthdate}')
        return False

def process_people(entries: list[tuple]) -> dict:
    good_count = 0
    bad_count = 0
    
    for entry in entries:
        # Распаковываем кортеж на имя и дату
        name, birthdate = entry
        
        # Проверяем запись и обновляем нужный счетчик
        if validate_record(name, birthdate):
            good_count += 1
        else:
            bad_count += 1
            
    # Возвращаем итоговую статистику
    return {'good': good_count, 'bad': bad_count}