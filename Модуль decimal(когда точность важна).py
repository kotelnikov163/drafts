from decimal import Decimal, getcontext
import math as m

getcontext().prec = 10  # 10 значащих цифр

def get_pond_info(a, b, depth):
    # Decimal(str(...)) — чтобы избежать ошибок float
    a, b, depth = Decimal(str(a)), Decimal(str(b)), Decimal(str(depth))
    pi = Decimal(str(m.pi))
    ellipse_area = pi * a * b      # площадь эллипса
    result = ellipse_area * depth  # объём = площадь × глубина
    return f"Площадь пруда: {ellipse_area} кв.м.\nКоличество воды: {result} куб.м."

print(get_pond_info(2.5, 1.75, 0.35))