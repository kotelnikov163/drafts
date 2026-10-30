def format_float_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Получаем результат функции
        
        if isinstance(result, float):   # Если это float...
            return round(result, 2)     # ...округляем до 2 знаков
            
        return result                   # Иначе возвращаем как есть
    return wrapper