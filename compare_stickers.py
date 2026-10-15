def get_stickers_comparison(collection_1, collection_2):
    """
    Сравнивает две коллекции стикеров и возвращает кортеж из трёх
    отсортированных списков:
    - стикеры, которые есть только в первой коллекции;
    - стикеры, которые есть только во второй коллекции;
    - стикеры, которые есть в обеих коллекциях.
    """
    first_stickers = set(collection_1)
    second_stickers = set(collection_2)

    only_in_first = first_stickers - second_stickers
    only_in_second = second_stickers - first_stickers
    in_both = first_stickers & second_stickers

    return (
        sorted(only_in_first),
        sorted(only_in_second),
        sorted(in_both),
    )


# Списки стикеров:
stas_collection = [
    'Тим Бернерс-Ли', 'Линус Торвальдс', 'Ада Лавлейс',
    'Линус Торвальдс', 'Маргарет Гамильтон', 'Бьярн Страуструп',
]
anton_collection = [
    'Тим Бернерс-Ли', 'Гвидо ван Россум', 'Линус Торвальдс',
    'Бьярн Страуструп', 'Бьярн Страуструп', 'Кен Томпсон', 'Деннис Ричи',
]

# Распаковываем результат в три переменные с говорящими именами:
only_stas, only_anton, both_have = get_stickers_comparison(
    stas_collection, anton_collection
)

print('Стикеры, которые есть только у Стаса:', only_stas)
print('Стикеры, которые есть только у Антона:', only_anton)
print('Стикеры, которые есть и у Стаса, и у Антона:', both_have)