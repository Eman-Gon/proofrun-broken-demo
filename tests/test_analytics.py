import unittest
from broken_shop.analytics import hourly_orders, delivery_windows, daily_revenue_ticks


class AnalyticsContractTests(unittest.TestCase):
    def test_hourly_orders_produces_24_ticks(self):
        self.assertEqual(len(hourly_orders()), 24)

    def test_delivery_windows_are_two_hours_apart(self):
        values = delivery_windows()
        self.assertEqual((values[1] - values[0]).total_seconds(), 7200)

    def test_revenue_ticks_are_three_hours_apart(self):
        values = daily_revenue_ticks()
        self.assertEqual((values[1] - values[0]).total_seconds(), 10800)
