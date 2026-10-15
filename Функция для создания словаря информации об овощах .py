def create_vegetable_info(vegetable_names, variety_names, yield_values):
    # Объединяем названия сортов с их урожайностью в пары
    variety_yield_pairs = list(zip(variety_names, yield_values))
    
    # Сопоставляем каждый овощ с его сортом и урожайностью
    vegetable_info = dict(zip(vegetable_names, variety_yield_pairs))
    
    return vegetable_info


# Тестовые данные:
vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]

# Вызов функции:
print(create_vegetable_info(vegetables, varieties, yields))