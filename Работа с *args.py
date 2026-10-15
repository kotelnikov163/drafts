def inspect_args(*args):
    print('Значение args:', args)
    print('Значение args[0]:', args[0])
    print('Длина args:', len(args))
    print()  # Пустая строка для читаемости вывода.

def inspect_kind_and_args(kind, *args):
    print('Значение kind:', kind)
    print('Значение args:', args)
    print('Значение args[0]:', args[0])
    print('Длина args:', len(args))

print('Вызвали функцию inspect_args():')
inspect_args('Овощи', 'Помидоры', 'Огурцы', 'Баклажаны', 'Перец')

print('Вызвали функцию inspect_kind_and_args():')
inspect_kind_and_args('Овощи', 'Помидоры', 'Огурцы', 'Баклажаны', 'Перец')