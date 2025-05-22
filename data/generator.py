
def generate_price_series(length=100, base_price=100):
    import random
    prices = [base_price]
    for _ in range(length - 1):
        prices.append(prices[-1] + random.uniform(-1, 1))
    return prices

