def obfuscator(func):
    def wrapper():
        # Вызываем исходную функцию и получаем словарь
        data = func()
        
        # Обрабатываем значение по ключу 'name'
        name = data['name']
        if len(name) > 2:
            data['name'] = name[0] + '*' * (len(name) - 2) + name[-1]
        else:
            # Если имя слишком короткое (1 или 2 символа), скрываем его полностью
            # (для 2 символов правило "первый и последний" оставит их как есть, 
            # но по логике скрытия лучше заменить, хотя в задаче пример с длинным именем)
            data['name'] = '*' * len(name) 
            
        # Обрабатываем значение по ключу 'password'
        password = data['password']
        data['password'] = '*' * len(password)
        
        # Возвращаем измененный словарь
        return data
    return wrapper