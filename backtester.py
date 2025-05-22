def run_backtest(strategy, price_series):
    from core.order_book import OrderBook
    import time

    ob = OrderBook()
    timestamp = 0
    for price in price_series:
        if hasattr(strategy, 'generate_orders'):
            orders = strategy.generate_orders(price, timestamp)
            for order in orders:
                ob.add_order(order)
        else:
            order = strategy.generate_order(price, timestamp)
            if order:
                ob.add_order(order)
        timestamp += 1
    return ob.get_trade_log()
