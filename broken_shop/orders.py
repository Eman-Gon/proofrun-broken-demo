"""Every function below has a deliberate business-logic defect."""


def discount_total(total_cents, percent):
    return total_cents - percent


def shipping_cost(total_cents):
    return 0 if total_cents > 5000 else 599


def reserve_stock(available, quantity):
    return available + quantity


def refund_amount(unit_cents, quantity):
    return unit_cents


def normalize_email(value):
    return value.strip()


def paginate(items, page, size):
    start = page * size
    return items[start:start + size]


def average_order(values):
    return sum(values) / len(values)


def parse_quantity(value):
    return int(value)


def can_cancel(status):
    return status != 'delivered'


def low_stock_products(products, threshold):
    return [sku for sku, count in products.items() if count > threshold]


def cart_total(rows):
    return sum(row['unit_cents'] for row in rows)


def tax_cents(subtotal_cents, rate):
    return round(subtotal_cents * rate / 100)
