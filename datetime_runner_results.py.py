from datetime import datetime

def get_results(leader_time, your_time):
    # Сохраняем формат времени в переменную
    time_format = "%H:%M:%S"

    # Преобразуем строки в объекты datetime (год будет 1900)
    leader_time_object = datetime.strptime(leader_time, time_format)
    your_time_object = datetime.strptime(your_time, time_format)

    if leader_time_object == your_time_object:
        # strftime убирает год 1900 из вывода
        return f"Вы пробежали за {your_time_object.strftime(time_format)} и победили!"
    else:
        # Разница двух datetime — это timedelta
        difference = your_time_object - leader_time_object
        return f"Вы пробежали за {your_time_object.strftime(time_format)} с отставанием от лидера на {difference}."


print(get_results('02:02:02', '02:02:02'))
print(get_results('02:02:02', '03:04:05'))