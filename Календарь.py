year = 2026

months = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
]


# Функция, вычисляющая количество дней в месяце.
def get_duration(year, month_index):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month_index == 1 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return 29
    return days_in_month[month_index]


# Функция, печатающая шапку месяца.
def print_header(year_value, month_index):
    print(months[month_index], year_value)
    print('Пн Вт Ср Чт Пт Сб Вс')


# Функция, вычисляющая день недели, который приходится на 1 января:
def get_starting_day(year):
    d = 1
    m = 13
    y = year - 1
    h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7


# Функция, вычисляющая день недели,
# на который выпадет первое число следующего месяца:
def adjust_start_day(start_day, days_in_month):
    result = (start_day + days_in_month) % 7
    return result


# Функция, печатающая дни месяца.
def print_days(days_in_month, start_day):
    # Печатаем пробелы для дней до начала месяца
    for _ in range(start_day):
        print('  ', end=' ')

    # Печатаем дни месяца
    for day in range(1, days_in_month + 1):
        print(f'{day:2}', end=' ')
        if (start_day + day) % 7 == 0:
            print()  # перенос строки после воскресенья

    # Если последний день месяца — не воскресенье,
    # печатаем дополнительную пустую строку
    if (days_in_month + start_day) % 7 != 0:
        print()


def print_calendar(year):
    start_day = get_starting_day(year)

    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration(year, month_number)
        print_days(duration, start_day)

        start_day = adjust_start_day(start_day, duration)
        print()


print_calendar(year)