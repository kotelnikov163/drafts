def analyze_results(data):
    # Шаг 1. Собираем суммарные баллы каждой команды в словарь scores.
    scores = {}
    for race in data:
        for team, score in race.items():
            if team in scores:
                # Команда уже встречалась — прибавляем очки.
                scores[team] += score
            else:
                # Команда новая — создаём запись.
                scores[team] = score

    # Выводим команды в алфавитном порядке.
    teams = sorted(scores)
    print('Команды, участвовавшие в чемпионате:')
    for team in teams:
        print(f'* {team}')

    # Шаг 2. Ищем команду с максимальным количеством баллов.
    winner_team = None
    winner_score = 0
    for team, score in scores.items():
        if score > winner_score:
            winner_score = score
            winner_team = team

    # Печатаем победителя.
    print(f'В чемпионате победила команда {winner_team} с результатом {winner_score} баллов')


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)