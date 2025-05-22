# main.py

from generator import generate_price_series
from backtest import run_backtest
from metrics import compute_metrics
from strategies.mean_reversion import MeanReversionStrategy
from strategies.momentum import MomentumStrategy
from strategies.market_maker import MarketMakingStrategy

def main():
    print("Choose strategy:")
    print("1. Mean Reversion")
    print("2. Momentum")
    print("3. Market Making")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == '1':
        strategy = MeanReversionStrategy()
    elif choice == '2':
        strategy = MomentumStrategy()
    elif choice == '3':
        strategy = MarketMakingStrategy()
    else:
        print("Invalid choice.")
        return

    prices = generate_price_series(length=100, base_price=100)
    trade_log = run_backtest(strategy, prices)
    metrics = compute_metrics(trade_log)

    print("\n--- Backtest Summary ---")
    print(f"Total Trades: {len(trade_log)}")
    print(f"Total Volume: {metrics['volume']}")
    print(f"Average Price: {metrics['avg_price']:.2f}")

if __name__ == "__main__":
    main()
