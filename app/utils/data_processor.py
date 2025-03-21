import pandas as pd

def calculate_indicators(data):
    """
    Calculate technical indicators from financial data.
    
    Args:
        data (dict): Financial data in dictionary format.
    
    Returns:
        dict: A dictionary containing calculated indicators.
    """
    df = pd.DataFrame(data)

    df['MA_20'] = df['close'].rolling(window=20).mean()
    df['MA_50'] = df['close'].rolling(window=50).mean()

    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    return df.to_dict('records')