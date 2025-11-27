# HL3 and LL3 Signal Detector

class SignalDetector:
    def __init__(self, price_data):
        self.price_data = price_data

    def detect_hl3(self):
        signals = []
        for i in range(2, len(self.price_data)):
            if (self.price_data[i] > self.price_data[i-1] and 
                self.price_data[i-1] > self.price_data[i-2]):
                signals.append((i, 'HL3'))  # Higher Low Signal
        return signals

    def detect_ll3(self):
        signals = []
        for i in range(2, len(self.price_data)):
            if (self.price_data[i] < self.price_data[i-1] and 
                self.price_data[i-1] < self.price_data[i-2]):
                signals.append((i, 'LL3'))  # Lower Low Signal
        return signals

# Example usage
if __name__ == "__main__":
    price_data = [1, 2, 3, 2, 1, 2, 3, 4]  # Replace with actual price data
    detector = SignalDetector(price_data)
    hl3_signals = detector.detect_hl3()
    ll3_signals = detector.detect_ll3()
    print("HL3 Signals:", hl3_signals)
    print("LL3 Signals:", ll3_signals)