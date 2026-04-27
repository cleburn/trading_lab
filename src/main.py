from collector import KalshiClient
from processor import DataProcessor

def run_pipeline():
    client = KalshiClient()
    processor = DataProcessor()

    #1 Collect
    tickers = ["BTC-2026", "ETH-2026", "SOL-2026"]
    raw_data = [client.get_market_data(t) for t in tickers]

    #2. Process
    avg_price = processor.get_summary(raw_data)

    #3. Output
    print(f"--- Pipeline Results ---")
    print(f"Processed {len(raw_data)} markets.")
    print(f"Average Market Price: {avg_price:.4f}")

if __name__ == "__main__":
    run_pipeline()
