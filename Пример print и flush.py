import time

# Без flush — текст может появиться только в конце
print("Загрузка", end="")
for i in range(5):
    time.sleep(1)
    print(".", end="")

# С flush — точки появляются каждую секунду
print("Загрузка", end="", flush=True)
for i in range(5):
    time.sleep(1)
    print(".", end="", flush=True)
print(" Готово!")