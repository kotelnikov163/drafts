from datetime import datetime, timedelta

def get_weekday_name(weekday_number):
    # Возвращаем название дня по его номеру
    if weekday_number == 0:
        return 'понедельник'
    elif weekday_number == 1:
        return 'вторник'
    elif weekday_number == 2:
        return 'среда'
    elif weekday_number == 3:
        return 'четверг'
    elif weekday_number == 4:
        return 'пятница'
    elif weekday_number == 5:
        return 'суббота'
    elif weekday_number == 6:
        return 'воскресенье'


def get_day_after_tomorrow(date_string):
    now = datetime.strptime(date_string, "%Y-%m-%d")  # строка -> datetime
    now_weekday = get_weekday_name(now.weekday())     # день недели сегодня
    day_after_tomorrow = now + timedelta(days=2)      # +2 дня
    day_after_tomorrow_weekday = get_weekday_name(day_after_tomorrow.weekday())
    return f'Сегодня {date_string}, {now_weekday}, а послезавтра - {day_after_tomorrow_weekday}.'


print(get_day_after_tomorrow('2024-01-01'))
print(get_day_after_tomorrow('2024-01-02'))
print(get_day_after_tomorrow('2024-01-03'))
print(get_day_after_tomorrow('2024-01-04'))
print(get_day_after_tomorrow('2024-01-05'))
print(get_day_after_tomorrow('2024-01-06'))