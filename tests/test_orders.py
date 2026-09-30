import unittest
from broken_shop import orders


class BusinessContractTests(unittest.TestCase):
    def test_ten_percent_discount(self):
        self.assertEqual(orders.discount_total(10000, 10), 9000)

    def test_free_shipping_at_threshold(self):
        self.assertEqual(orders.shipping_cost(5000), 0)

    def test_reservation_decreases_stock(self):
        self.assertEqual(orders.reserve_stock(10, 3), 7)

    def test_refund_includes_every_unit(self):
        self.assertEqual(orders.refund_amount(250, 3), 750)

    def test_email_normalization(self):
        self.assertEqual(orders.normalize_email('  ADA@EXAMPLE.INVALID '), 'ada@example.invalid')

    def test_first_page_is_one_based(self):
        self.assertEqual(orders.paginate(['a', 'b', 'c', 'd'], 1, 2), ['a', 'b'])

    def test_empty_average_is_zero(self):
        self.assertEqual(orders.average_order([]), 0)

    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValueError):
            orders.parse_quantity('-2')

    def test_shipped_order_cannot_be_cancelled(self):
        self.assertFalse(orders.can_cancel('shipped'))

    def test_low_stock_includes_threshold(self):
        self.assertEqual(orders.low_stock_products({'a': 0, 'b': 3, 'c': 8}, 3), ['a', 'b'])

    def test_cart_multiplies_quantities(self):
        self.assertEqual(orders.cart_total([{'unit_cents': 200, 'quantity': 3}]), 600)

    def test_tax_rate_is_fraction(self):
        self.assertEqual(orders.tax_cents(10000, 0.08), 800)
