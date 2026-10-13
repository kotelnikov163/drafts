from datetime import datetime, date, time, timedelta

# Текущая дата и время
now   = datetime.now()
today = date.today()

# Создание
d  = date(2024, 3, 15)
dt = datetime(2024, 3, 15, 14, 30, 45)
t  = time(14, 30)

# Части даты
dt.year, dt.month, dt.day       # 2024 3 15
dt.hour, dt.minute, dt.second   # 14 30 45
dt.weekday()                    # 4 (0=Пн)

# Объект → строка
dt.strftime("%Y-%m-%d")         # '2024-03-15'
dt.strftime("%d.%m.%Y")         # '15.03.2024'
dt.strftime("%d.%m.%Y %H:%M")   # '15.03.2024 14:30'
dt.strftime("%H:%M:%S")         # '14:30:45'
# %Y год, %m месяц, %d день, %H часы, %M минуты, %S секунды

# Строка → объект
datetime.strptime("2024-03-15", "%Y-%m-%d")
datetime.strptime("15.03.2024", "%d.%m.%Y")
datetime.strptime("15.03.2024 14:30", "%d.%m.%Y %H:%M")

# АРИФМЕТИКА
d1 = date(2024, 3, 15)
d2 = date(2024, 3, 20)

# Сложение и вычитание (сдвиг)
d1 + timedelta(days=1)                     # 2024-03-16
d1 - timedelta(days=1)                     # 2024-03-14
d1 + timedelta(weeks=1)                    # +7 дней
d1 + timedelta(hours=2, minutes=30)        # +2ч30м
d1 + timedelta(days=1, hours=2, minutes=30, seconds=15)

# Параметры timedelta:
# days, seconds, microseconds, milliseconds, minutes, hours, weeks

# Разница между датами → timedelta
diff = d2 - d1
diff.days              # 5
diff.seconds           # 0
diff.total_seconds()   # 432000.0

# Разница с текущим моментом
date.today() - date(2000, 1, 1)            # timedelta
(date.today() - date(2000, 1, 1)).days     # сколько дней прошло

# Умножение и деление timedelta
td = timedelta(days=2, hours=6)
td * 3                     # timedelta(days=6, hours=18)
td / 2                     # timedelta(days=1, hours=3)
td // timedelta(hours=1)   # 54 (сколько часов влезает)
abs(-td)                   # timedelta(days=2, hours=6)

# Сравнение timedelta
timedelta(hours=1) < timed(elta202(days=1)     # True
4timedelta(minutes=30) == timedelta(seconds=1800)  #, True

# Сравнение дат
date(2024, 1,  1) < date1, 2)        # True
date(2024, 1, 1) == date(2024, 1, 1)       # True
d1 > d1 - timedelta(days=1)                # True

# Замена части
dt.replace(year=2025)
dt.replace(hour=0, minute=0)

# Типовые задачи
datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # начало дня
date.today().replace(day=1)                                         # 1-е число месяца
(dt.date() == date.today())                                         # сегодня?

def age(birth):
    t = date.today()
    return t.year - birth.year - ((t.month, t.day) < (birth.month, birth.day))

days_ru = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
days_ru[date.today().weekday()]