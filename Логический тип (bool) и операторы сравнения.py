# Хорошо:
user_age = None  # Пока неизвестно
print(user_age is None)

# Плохо:
print(user_age == None) # неявное сравнение булевого значения

# Плохо:
x = 5
print((x > 5) == True)

# Хорошо:
print(x > 5)


age = 20
has_access = True

# Хорошо (скобки для ясности):
if (age >= 18) and has_access:
    print("Доступ разрешён")

# Плохо (без скобок):
if age >= 18 and has_access:  # Работает, но менее читаемо
    print("Доступ разрешён")


def is_valid_password(password: str) -> bool:
    """Проверяет, соответствует ли пароль требованиям."""
    return (len(password) >= 8) and ("!" in password)

print(is_valid_password("qwerty"))  # False
print(is_valid_password("qwerty123!"))  # True