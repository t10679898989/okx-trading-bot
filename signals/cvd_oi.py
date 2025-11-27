import pandas as pd
import numpy as np

class CVD_OI_Analyzer:
    def __init__(self, data):
        self.data = data

    def calculate_cvd(self):
        # Cumulative Volume Delta calculation
        self.data['CVD'] = (self.data['buy_volume'] - self.data['sell_volume']).cumsum()
        return self.data['CVD']

    def calculate_oi_signals(self):
        # Open Interest analysis logic
        self.data['OI_Signal'] = np.where(self.data['open_interest'].diff() > 0, 'Increase', 'Decrease')
        return self.data['OI_Signal']

    def analyze(self):
        self.calculate_cvd()
        self.calculate_oi_signals()
        return self.data[['CVD', 'OI_Signal']]

if __name__ == '__main__':
    # Example of usage
    # Replace with actual data loading
    df = pd.DataFrame({
        'buy_volume': [100, 200, 150],
        'sell_volume': [80, 120, 100],
        'open_interest': [1000, 1020, 1010]
    })
    analyzer = CVD_OI_Analyzer(df)
    signals = analyzer.analyze()
    print(signals)