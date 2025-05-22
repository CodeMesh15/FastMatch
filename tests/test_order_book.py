def test_order_book_matching():
    from core.order_book import OrderBook
    from core.order import Order, Side, OrderType

    ob = OrderBook()
    ob.add_order(Order(price=100, quantity=1, side=Side.BUY, order_type=OrderType.LIMIT, timestamp=0))
    ob.add_order(Order(price=99, quantity=1, side=Side.SELL, order_type=OrderType.LIMIT, timestamp=1))

    assert len(ob.get_trade_log()) == 1
