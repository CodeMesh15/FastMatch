import random
import time
from core.order import Order, Side, OrderType

class MeanReversionStrategy:
    def __init__(self, mean_price=100, threshold=2):
        self.mean_price = mean_price
        self.threshold = threshold

    def generate_order(self, current_price, timestamp):
        if current_price < self.mean_price - self.threshold:
            return Order(price=current_price, quantity=1, side=Side.BUY, order_type=OrderType.LIMIT, timestamp=timestamp)
        elif current_price > self.mean_price + self.threshold:
            return Order(price=current_price, quantity=1, side=Side.SELL, order_type=OrderType.LIMIT, timestamp=timestamp)
        return None
