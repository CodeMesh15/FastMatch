class MomentumStrategy:
    def __init__(self, window_size=3):
        self.prices = []
        self.window_size = window_size

    def generate_order(self, current_price, timestamp):
        self.prices.append(current_price)
        if len(self.prices) < self.window_size:
            return None
        trend = all(self.prices[i] < self.prices[i+1] for i in range(-self.window_size, -1))
        if trend:
            return Order(price=current_price, quantity=1, side=Side.BUY, order_type=OrderType.MARKET, timestamp=timestamp)
        elif all(self.prices[i] > self.prices[i+1] for i in range(-self.window_size, -1)):
            return Order(price=current_price, quantity=1, side=Side.SELL, order_type=OrderType.MARKET, timestamp=timestamp)
        return None
