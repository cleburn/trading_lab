class DataProcessor:
    """A simple processor to handle market data."""

    def calculate_mid(self, price, volume):
        # Let's simplify: just return the price for now
        # or do a mock calculation
        return price * 1.0

    def get_summary(self, data_list):
        """Calculate average price from a list of market data dicts."""
        if not data_list:
            return 0
        total_price = sum(d['price'] for d in data_list)
        return total_price / len(data_list)
