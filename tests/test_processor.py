from processor import DataProcessor

def test_calculate_mid():
    p = DataProcessor()
    assert p.calculate_mid(0.5, 100) == 0.5

def test_get_summary():
    p = DataProcessor()
    data = [{"price": 0.1}, {"price": 0.3}]
    assert p.get_summary(data) == 0.2
