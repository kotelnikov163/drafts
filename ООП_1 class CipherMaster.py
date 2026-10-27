class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        
        # Если is_encrypt == False (то есть мы дешифруем), 
        # то сдвиг должен быть в обратную сторону. 
        # Поэтому просто меняем знак shift на противоположный.
        if not is_encrypt:
            shift = -shift
            
        # Приводим весь входящий текст к нижнему регистру, 
        # как того требует задание
        for letter in text.lower():
            
            # Проверяем, есть ли буква в алфавите (отсеиваем пробелы и знаки)
            if letter in self.alphabet:
                # Находим индекс буквы (теперь без .lower(), так как текст уже в нижнем регистре)
                index = self.alphabet.index(letter)
                
                # Считаем новый индекс с защитой от выхода за границы (%)
                new_index = (index + shift) % len(self.alphabet)
                
                # Добавляем новую зашифрованную/расшифрованную букву
                result.append(self.alphabet[new_index])
            else:
                # Если символ не в алфавите, оставляем его как есть
                result.append(letter)
                
        # Склеиваем список в строку и возвращаем
        return ''.join(result)