import ccxt

class OKXAPI:
    def __init__(self, api_key, secret, password):
        self.exchange = ccxt.okex({
            'apiKey': api_key,
            'secret': secret,
            'password': password,
        })

    def fetch_candle_data(self, symbol, timeframe='1m', since=None, limit=100):
        """
        Fetch candle data for a given symbol and timeframe.
        :param symbol: Trading pair symbol (e.g., 'BTC/USDT')
        :param timeframe: Timeframe for the candles (e.g., '1m', '5m', '1h')
        :param since: Timestamp to fetch candles from
        :param limit: Number of candles to fetch
        :return: List of candle data
        """
        return self.exchange.fetch_ohlcv(symbol, timeframe, since, limit)

    def place_order(self, symbol, order_type, side, amount, price=None):
        """
        Place an order on the exchange.
        :param symbol: Trading pair symbol (e.g., 'BTC/USDT')
        :param order_type: Type of the order ('market' or 'limit')
        :param side: Side of the order ('buy' or 'sell')
        :param amount: Amount of the asset to buy/sell
        :param price: The price for limit orders
        :return: Order response
        """
        return self.exchange.create_order(symbol, order_type, side, amount, price)

    def get_open_positions(self):
        """
        Retrieve current open positions.
        :return: List of open positions
        """
        return self.exchange.fetch_positions() if hasattr(self.exchange, 'fetch_positions') else []
