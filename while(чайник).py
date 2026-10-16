from random import randint

# Начальная температура чая
current_temperature = 85

while current_temperature > 60:
    t = randint(1, 3)
    current_temperature -= t
    print(f'Прошла минута.\nЧай остыл ещё на {t} °C. Текущая температура: {current_temperature} °C')
print('Время пить чай!')
    