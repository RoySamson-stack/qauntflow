import requests
import pandas as pd
from datetime import datetime
from ..config import ALPHA_VANTAGE_API_KEY, BINANCE_API_KEY

def fetch_stock_data(symbol, interval='1d'):
    """Fetch stock data from Alpha Vantage"""
    function = 'TIME_SERIES_DAILY' if interval == '1d' else 'TIME_SERIES_INTRADAY'
    
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    if interval != '1d':
        url += f'&interval={interval}'
    
    response = requests.get(url)
    data = response.json()
    
    time_series = data.get('Time Series (Daily)', data.get(f'Time Series ({interval})', {}))
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    df.columns = [col.split(' ')[1].lower() for col in df.columns]
    
    return df.sort_index()

def fetch_crypto_data(symbol, interval='1d'):
    """Fetch cryptocurrency data from Binance"""
    base_url = 'https://api.binance.com/api/v3/klines'
    interval_map = {
        '1m': '1m',
        '5m': '5m',
        '15m': '15m',
        '30m': '30m',
        '1h': '1h',
        '4h': '4h',
        '1d': '1d'
    }
    
    params = {
        'symbol': symbol,
        'interval': interval_map.get(interval, '1d'),
        'limit': 1000
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Parse Binance data
    df = pd.DataFrame(data, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    
    # Convert to proper types
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
    df.set_index('open_time', inplace=True)
    numeric_cols = ['open', 'high', 'low', 'close', 'volume']
    df[numeric_cols] = df[numeric_cols].astype(float)
    
    return df[numeric_cols]