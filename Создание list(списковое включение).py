# Сперва решим эту задачу в обычном цикле
new_sequence = []

for value in range(6):
    list.append(new_sequence, value * 3)

print(new_sequence)

# А теперь то же самое запишем в сокращённой форме:
new_sequence_better = [value * 3 for value in range(6)] # Всё!
print(new_sequence_better)