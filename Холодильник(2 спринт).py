import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    """Добавляет партию продукта. Мутирует items."""
    if title not in items:
        items[title] = []
    if expiration_date is not None:
        expiration_date = dt.datetime.strptime(expiration_date, DATE_FORMAT).date()
    items[title].append({
        'amount': Decimal(str(amount)),  # str() — чтобы не ловить float-погрешности
        'expiration_date': expiration_date,
    })
    return items


def add_by_note(items, note):
    """Парсит '<название> <кол-во> [<дата>]'. Мутирует items."""
    parts = note.split()

    try:
        dt.datetime.strptime(parts[-1], DATE_FORMAT)
        is_date = True
    except ValueError:
        is_date = False

    if is_date:
        expiration_date = parts[-1]
        amount = parts[-2]
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = parts[-1]
        title = ' '.join(parts[:-1])

    add(items, title, amount, expiration_date)


def find(items, needle):
    """Названия продуктов, содержащие подстроку (без учёта регистра)."""
    needle_lower = needle.lower()
    return [title for title in items if needle_lower in title.lower()]


def get_amount(items, needle):
    """Суммарное количество по всем найденным продуктам."""
    total = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            total += part['amount']
    return total


def get_expired(items, in_advance_days=0):
    """(название, количество) для партий со сроком <= today + N дней."""
    today = dt.date.today()
    deadline = today + dt.timedelta(days=in_advance_days)
    result = []

    for title, parts in items.items():
        amount = Decimal('0')
        for part in parts:
            exp = part['expiration_date']
            if exp is not None and exp <= deadline:  # None = без срока, не считаем
                amount += part['amount']
        if amount > 0:
            result.append((title, amount))

    return result