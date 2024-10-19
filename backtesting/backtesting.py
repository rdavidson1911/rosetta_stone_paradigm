import pandas as pd
import numpy as np
from typing import List, Tuple, Callable

class Strategy:
    def __init__(self, name: str, entry: Callable, exit: Callable):
        self.name = name
        self.entry = entry
        self.exit = exit

class Backtester:
    def __init__(self, data: pd.DataFrame, initial_capital: float = 10000):
        self.data = data
        self.initial_capital = initial_capital

    def run(self, strategy: Strategy) -> pd.DataFrame:
        signals = pd.DataFrame(index=self.data.index)
        signals['signal'] = 0
        signals['entry'] = strategy.entry(self.data)
        signals['exit'] = strategy.exit(self.data)
        
        signals['signal'] = np.where(signals['entry'], 1, 0)
        signals['signal'] = np.where(signals['exit'], 0, signals['signal'])
        signals['position'] = signals['signal'].diff()

        portfolio = pd.DataFrame(index=signals.index)
        portfolio['holdings'] = (self.data['Close'] * signals['signal']).diff()
        portfolio['cash'] = -portfolio['holdings'] * self.data['Close']
        portfolio['total'] = self.initial_capital + portfolio['cash'].cumsum() + (signals['signal'] * self.data['Close'])

        return portfolio

def simple_moving_average_strategy(data: pd.DataFrame, short_window: int = 50, long_window: int = 200) -> Strategy:
    def entry(data: pd.DataFrame) -> pd.Series:
        short_ma = data['Close'].rolling(window=short_window).mean()
        long_ma = data['Close'].rolling(window=long_window).mean()
        return short_ma > long_ma

    def exit(data: pd.DataFrame) -> pd.Series:
        short_ma = data['Close'].rolling(window=short_window).mean()
        long_ma = data['Close'].rolling(window=long_window).mean()
        return short_ma < long_ma

    return Strategy("Simple Moving Average", entry, exit)

# Example usage
if __name__ == "__main__":
    # Load your data here (e.g., from a CSV file or an API)
    data = pd.read_csv("path/to/your/data.csv", index_col='Date', parse_dates=True)
    
    backtester = Backtester(data)
    sma_strategy = simple_moving_average_strategy(data)
    results = backtester.run(sma_strategy)
    
    print(results.tail())
