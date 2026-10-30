def outer_function(func):
    # Вызываем функцию, полученную в аргументе func
    result = func('Стас')
    print(result)


def say_hello(name):
    return f'Привет, {name}!'


# Передаём say_hello как объект - без скобок!
outer_function(say_hello)