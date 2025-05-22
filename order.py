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
