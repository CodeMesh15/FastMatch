class MarketMakingStrategy:
    def __init__(self, spread=1.0):
        self.spread = spread

    def generate_orders(self, mid_price, timestamp):
        buy_order = Order(price=mid_price - self.spread / 2, quantity=1, side=Side.BUY, order_type=OrderType.LIMIT, timestamp=timestamp)
        sell_order = Order(price=mid_price + self.spread / 2, quantity=1, side=Side.SELL, order_type=OrderType.LIMIT, timestamp=timestamp)
        return [buy_order, sell_order]
