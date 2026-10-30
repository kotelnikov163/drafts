class User:
    def __init__(
            self,
            first_name: str | None = None,
            last_name: str | None = None,
            username: str | None = None,
    ):
        # Проверяем, что хотя бы один параметр передан
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        # Сохраняем переданные значения в атрибуты объекта
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Альтернативный конструктор: создаёт пользователя по имени и фамилии.
    # cls — это ссылка на сам класс User (а не на экземпляр),
    # поэтому внутри метода можно вызвать cls(...) и получить новый объект.
    @classmethod
    def with_name(
            cls,
            first_name: str,
            last_name: str,
    ) -> 'User':
        # Создаём новый экземпляр User, передавая имя и фамилию в конструктор.
        # username остаётся None — пользователь зарегистрирован по имени.
        return cls(first_name=first_name, last_name=last_name)

    # Альтернативный конструктор: создаёт пользователя по псевдониму.
    @classmethod
    def with_username(
            cls,
            username: str,
    ) -> 'User':
        # Сначала проверяем псевдоним на безопасность через статический метод.
        # Если псевдоним начинается с 'admin' — is_username_allowed вернёт False.
        if not cls.is_username_allowed(username):
            # Некорректный псевдоним — прерываем создание объекта исключением.
            raise ValueError('Некорректное имя пользователя')
        # Псевдоним безопасен — создаём пользователя только с username.
        return cls(username=username)

    # Статический метод: не зависит ни от экземпляра, ни от класса.
    # Это просто утилитарная проверка, которую можно вызывать отдельно.
    @staticmethod
    def is_username_allowed(username: str) -> bool:
        # startswith проверяет, начинается ли строка с подстроки 'admin'.
        # not инвертирует результат: True — если псевдоним НЕ начинается с 'admin'.
        return not username.startswith('admin')

    # Свойство: доступно как атрибут (stas.full_name), без вызова скобками.
    @property
    def full_name(self) -> str:
        # Приоритет отдаём имени и фамилии, если они заданы.
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        # Иначе, если задан псевдоним — возвращаем его с символом @.
        elif self.username:
            return f'@{self.username}'
        # Запасной вариант (по логике __init__ недостижим, но для полноты).
        return ''


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)  # Ожидаемый вывод: Стас Басов

# При отправке задания оставьте эту часть закомментированной.
# Попробуем создать пользователя с "запрещённым" именем.
# ne_stas = User.with_username('admin_nestas_anonymous')