vegetable_yields = [6.5, 4.3, 2.8, -3.8, 2.2, 3.5]

# Все ли проверки вернули True?
are_all_positive = all([vegetable_yield > 0 for vegetable_yield in vegetable_yields])

# Есть ли хоть один элемент, вернувший True?
are_any_positive = any([vegetable_yield > 0 for vegetable_yield in vegetable_yields])

print('Все ли элементы вернули True?', are_all_positive)
print('Есть ли хоть один элемент, вернувший True?', are_any_positive)