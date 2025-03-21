import requests
from app.config import ALPHA_VANTAGE_API_KEY

def fetch_data(symbol, interval='1d'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data