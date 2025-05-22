from enum import Enum
import uuid
from dataclasses import dataclass, field
from typing import Optional

class OrderType(Enum):
    MARKET = 'market'
    LIMIT = 'limit'

class Side(Enum):
    BUY = 'buy'
    SELL = 'sell'

@dataclass(order=True)
class Order:
    price: Optional[float]  # None for market orders
    quantity: float
    side: Side
    order_type: OrderType
    timestamp: float  # Use for tie-breaking
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __repr__(self):
        return f"Order(id={self.id[:8]}, side={self.side.name}, type={self.order_type.name}, qty={self.quantity}, price={self.price}, time={self.timestamp})"


# PART 2: BASIC ORDER BOOK ENGINE
# ================================
# order_book.py

import heapq
import time

class OrderBook:
    def __init__(self):
        self.bids = []  # max-heap for buys
        self.asks = []  # min-heap for sells
        self.trade_log = []

    def _match(self):
        while self.bids and self.asks:
            best_bid = self.bids[0][1]
            best_ask = self.asks[0][1]
            
            if best_bid.price >= best_ask.price:
                traded_price = best_ask.price
                traded_quantity = min(best_bid.quantity, best_ask.quantity)

                best_bid.quantity -= traded_quantity
                best_ask.quantity -= traded_quantity
                
                self.trade_log.append((time.time(), traded_price, traded_quantity))

                if best_bid.quantity == 0:
                    heapq.heappop(self.bids)
                if best_ask.quantity == 0:
                    heapq.heappop(self.asks)
            else:
                break

    def add_order(self, order: Order):
        if order.order_type == OrderType.MARKET:
            # Market orders match instantly
            if order.side == Side.BUY:
                while self.asks and order.quantity > 0:
                    best_ask = self.asks[0][1]
                    traded_quantity = min(order.quantity, best_ask.quantity)
                    order.quantity -= traded_quantity
                    best_ask.quantity -= traded_quantity
                    self.trade_log.append((time.time(), best_ask.price, traded_quantity))
                    if best_ask.quantity == 0:
                        heapq.heappop(self.asks)
            elif order.side == Side.SELL:
                while self.bids and order.quantity > 0:
                    best_bid = self.bids[0][1]
                    traded_quantity = min(order.quantity, best_bid.quantity)
                    order.quantity -= traded_quantity
                    best_bid.quantity -= traded_quantity
                    self.trade_log.append((time.time(), best_bid.price, traded_quantity))
                    if best_bid.quantity == 0:
                        heapq.heappop(self.bids)
        else:
            # Limit order: add to book
            item = (order.price if order.side == Side.SELL else -order.price, order)
            if order.side == Side.BUY:
                heapq.heappush(self.bids, item)
            else:
                heapq.heappush(self.asks, item)
            self._match()

    def get_depth(self):
        return {
            'bids': [(o.price, o.quantity) for _, o in sorted(self.bids, reverse=True)],
            'asks': [(o.price, o.quantity) for _, o in sorted(self.asks)]
        }

    def get_trade_log(self):
        return self.trade_log
