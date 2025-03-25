from ..config import BINANCE_API_KEY, BINANCE_SECRET_KEY, MAX_TRADE_AMOUNT, RISK_PERCENTAGE
import hmac
import hashlib
import requests
import time
import json
from urllib.parse import urlencode

def execute_trade(user_id, symbol, action, amount):
    """Execute a trade on Binance (simulated in this example)"""
    #  connect to the exchange API
    
    # Validate amount
    if amount > MAX_TRADE_AMOUNT:
        raise ValueError(f"Trade amount exceeds maximum of {MAX_TRADE_AMOUNT}")
    
    current_price = get_current_price(symbol)
    
    risk_amount = amount * (RISK_PERCENTAGE / 100)
    quantity = risk_amount / current_price
    
    trade_result = {
        'symbol': symbol,
        'action': action,
        'quantity': quantity,
        'price': current_price,
        'timestamp': int(time.time())
    }
    
    return trade_result

def get_current_price(symbol):
    """Get current price from Binance (simulated)"""
    #  call the Binance API
    import random
    return round(100 * (1 + (random.random() - 0.5) / 10), 2)

def real_binance_request(endpoint, params=None, method='GET'):
    base_url = 'https://api.binance.com'
    headers = {
        'X-MBX-APIKEY': BINANCE_API_KEY
    }
    
    if params is None:
        params = {}
    
    params['timestamp'] = int(time.time() * 1000)
    query_string = urlencode(params)
    signature = hmac.new(
        BINANCE_SECRET_KEY.encode('utf-8'),
        query_string.encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    url = f"{base_url}{endpoint}?{query_string}&signature={signature}"
    
    if method == 'GET':
        response = requests.get(url, headers=headers)
    else:
        response = requests.post(url, headers=headers)
    
    return response.json()