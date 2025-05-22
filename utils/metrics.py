def compute_metrics(trade_log):
    total_volume = sum(qty for _, _, qty in trade_log)
    average_price = sum(price * qty for _, price, qty in trade_log) / total_volume if total_volume else 0
    return {'volume': total_volume, 'avg_price': average_price}
