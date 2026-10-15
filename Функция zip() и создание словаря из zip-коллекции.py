vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
vegetable_yields = [6.5, 4.3, 2.8, 2.2, 3.5]
vegetable_varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']

# Передаём в аргументы функции zip() три последовательности:
zip_collection = zip(vegetables, vegetable_yields, vegetable_varieties)

print('Получили значение такого типа:', type(zip_collection))
print('Напечатать это значение нельзя:', zip_collection)

# Приводим значение zip к списку:
list_from_zip = list(zip_collection)

# Печатаем получившийся список:
print('list_from_zip =', list_from_zip)