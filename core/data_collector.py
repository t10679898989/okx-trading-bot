import requests
import pandas as pd
from datetime import datetime, timedelta

class DataCollector:
    def __init__(self, trading_pairs, timeframes):
        self.trading_pairs = trading_pairs
        self.timeframes = timeframes
        self.cache = {}

    def fetch_data(self, pair, timeframe):
        # Example API endpoint (to be modified based on the actual API)
        url = f'https://api.example.com/data?pair={{pair}}&timeframe={{timeframe}}'
        response = requests.get(url)
        data = response.json()  # Depending on the API response format
        return pd.DataFrame(data)

    def cache_data(self, pair, timeframe):
        key = f'{pair}_{timeframe}'
        if key not in self.cache:
            self.cache[key] = self.fetch_data(pair, timeframe)

    def get_cached_data(self, pair, timeframe):
        self.cache_data(pair, timeframe)
        return self.cache[f'{pair}_{timeframe}']

if __name__ == '__main__':
    pairs = ['BTC/USD', 'ETH/USD']
    timeframes = ['1m', '5m', '1h']
    collector = DataCollector(pairs, timeframes)

    # Example usage
    for pair in pairs:
        for timeframe in timeframes:
            data = collector.get_cached_data(pair, timeframe)
            print(f'Data for {{pair}} at {{timeframe}}:')
            print(data.head())
