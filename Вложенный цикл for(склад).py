data = {
    'яблоки': [
        {'quantity': 50, 'price': 100},
        {'quantity': 30, 'price': 90}
    ],
    'бананы': [
        {'quantity': 40, 'price': 80}
    ],
    'апельсины': [
        {'quantity': 20, 'price': 120},
        {'quantity': 25, 'price': 110}
    ]
}


def calculate_total_cost(stock):
    result = []

    for product_name, batches in stock.items():
        total_cost = 0
    
        for batch in batches:
            quantity = batch['quantity']
            price = batch['price']
            total_cost = total_cost + quantity * price
    
        if total_cost > 0:
            result.append((product_name, total_cost))

    return result


total = calculate_total_cost(data)
print(total)