def get_num(prompt, num_type=float):
    """Запрашивает число с проверкой. num_type: int или float."""
    while True:
        try:
            return num_type(input(prompt).replace(",", "."))
        except ValueError:
            print(f"Ошибка: введите {'целое число' if num_type is int else 'число'}!")


print("=== Калькулятор калорий ===\n")

age = get_num("Возраст: ", int)
weight = get_num("Вес (кг): ")
height = get_num("Рост (см): ")
workouts = get_num("Тренировок в неделю: ", int)

# BMR по формуле Миффлина-Сан Жеора (для мужчин)
bmr = 10 * weight + 6.25 * height - 5 * age + 5

# Коэффициент активности
if workouts == 0:
    coef = 1.2
elif workouts <= 2:
    coef = 1.375
elif workouts <= 4:
    coef = 1.55
else:
    coef = 1.725

tdee = bmr * coef

print("\n--- Результат ---")
print(f"BMR:  {bmr:.0f} ккал")
print(f"TDEE: {tdee:.0f} ккал")