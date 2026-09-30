import pandas as pd


def hourly_orders():
    return pd.date_range('2026-01-01', periods=24, freq='H')


def delivery_windows():
    return pd.timedelta_range(start='0 days', periods=4, freq='2H')


def daily_revenue_ticks():
    return pd.date_range('2026-01-01', periods=8, freq='3H')
