def get_selection(collection):
    # Сортируем копию коллекции по возрастанию, чтобы не менять исходный список
    sorted_collection = sorted(collection)

    # Определяем, сколько элементов нужно отбросить с каждой стороны (10% от общего числа)
    trim_count = len(sorted_collection) // 10

    # Вычисляем индекс, до которого (не включая) берём элементы среза
    end_index = len(sorted_collection) - trim_count

    # Возвращаем срез без первых trim_count и последних trim_count элементов
    result = sorted_collection[trim_count:end_index]
    return result
    
heights = [140.1, 150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1, 180]

# get_selection отбрасывает по 10% наименьших и наибольших значений,
# возвращая "усечённую" выборку без выбросов по краям
selection = get_selection(heights)
print('Выборка:', selection)