class Product:
    # Конструктор класса (инициализация экземпляра)
    def __init__(self, name, retail_price, purchase_price):
        self.name = name                      # Атрибут: название товара (строка)
        self.retail_price = retail_price      # Атрибут: розничная цена (число)
        self.purchase_price = purchase_price  # Атрибут: закупочная цена (число)

    # Свойство, которое вычисляет прибыль (не требует вызова со скобками)
    @property
    def profit(self):
        # Разница между розничной и закупочной ценой
        return self.retail_price - self.purchase_price

    # Статический метод (не зависит от конкретного экземпляра класса)
    @staticmethod
    def average_price(prices=None):
        # Проверяем, передан ли список цен и не пуст ли он
        # Если список не передан (None) или пуст [], возвращаем 0
        if not prices:
            return 0
        
        # Вычисляем среднее арифметическое: сумма всех цен / количество цен
        # Возвращаем результат в виде числа с плавающей точкой (float)
        return sum(prices) / len(prices)

    # Свойство, которое возвращает строку с полной информацией о товаре
    @property
    def information(self):
        # Используем f-строку для подстановки значений атрибутов.
        # ВАЖНО: используем обычный дефис (-) и соблюдаем пробелы, 
        # как в шаблоне из сообщения об ошибке системы.
        return (f"название - {self.name}, розничная цена - {self.retail_price}, "
                f"закупочная цена - {self.purchase_price}")