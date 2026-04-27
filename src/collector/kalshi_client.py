import random

class KalshiClient:
    """A mocked client for Kalshi to practice architectural patterns."""

    def __init__(self, environment="sandbox"):
        self.env = environment
        self.base_url = f"https://{environment}.kalshi.com/v2"
        print(f"Initialized {self.env} client.")

    def get_market_data(self, market_ticker):
        """Simulates fetching data for a specific market."""
        # In a real app, this would use the 'requests' library
        print(f"Fetching data for {market_ticker}...")
        return {
            "ticker": market_ticker,
            "price": round(random.random(), 2),
            "volume": random.randint(100, 10000)
        }

if __name__ == "__main__":
    # This allows you to test the file directly
    client = KalshiClient()
    print(client.get_market_data("BTC-26APR24"))
