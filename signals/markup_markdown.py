import pandas as pd

class MarketPhaseDetector:
    def __init__(self, price_data):
        self.price_data = price_data

    def detect_markup_phase(self):
        # Assuming price_data is a DataFrame with a column 'Close' for closing prices
        self.price_data['Markup'] = self.price_data['Close'].rolling(window=5).max().shift(1) < self.price_data['Close']
        return self.price_data[self.price_data['Markup']]

    def detect_markdown_phase(self):
       
        self.price_data['Markdown'] = self.price_data['Close'].rolling(window=5).min().shift(1) > self.price_data['Close']
        return self.price_data[self.price_data['Markdown']]

# Example Usage:
# price_data = pd.DataFrame({'Close': [100, 102, 101, 105, 107, 103, 99]})
# detector = MarketPhaseDetector(price_data)
# markup = detector.detect_markup_phase()
# markdown = detector.detect_markdown_phase()