
def test_order_repr():
    from core.order import Order, Side, OrderType
    o = Order(price=100, quantity=5, side=Side.BUY, order_type=OrderType.LIMIT, timestamp=0)
    assert "Order" in repr(o)
