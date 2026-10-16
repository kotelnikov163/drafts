def analyze_results(data):
    # Собираем названия всех команд из всех словарей в списке data.
    # Используем set, чтобы убрать дубликаты, затем сортируем по алфавиту.
    teams = sorted({team for race in data for team in race})
    
    print('Команды, участвовавшие в чемпионате:')
    for team in teams:
        print(f'* {team}')


races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)