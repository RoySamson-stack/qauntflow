import pandas as pd
import talib

def calculate_technical_indicators(df, indicators):
    """Calculate technical indicators for the given DataFrame"""
    results = df.copy()
    
    for indicator in indicators:
        indicator = indicator.strip().lower()
        
        if indicator == 'sma':
            results['sma_20'] = talib.SMA(results['close'], timeperiod=20)
            results['sma_50'] = talib.SMA(results['close'], timeperiod=50)
        elif indicator == 'ema':
            results['ema_20'] = talib.EMA(results['close'], timeperiod=20)
        elif indicator == 'rsi':
            results['rsi_14'] = talib.RSI(results['close'], timeperiod=14)
        elif indicator == 'macd':
            macd, macdsignal, macdhist = talib.MACD(
                results['close'], 
                fastperiod=12, 
                slowperiod=26, 
                signalperiod=9
            )
            results['macd'] = macd
            results['macd_signal'] = macdsignal
            results['macd_hist'] = macdhist
        elif indicator == 'bollinger':
            upper, middle, lower = talib.BBANDS(
                results['close'],
                timeperiod=20,
                nbdevup=2,
                nbdevdn=2,
                matype=0
            )
            results['bb_upper'] = upper
            results['bb_middle'] = middle
            results['bb_lower'] = lower
    
    return results.dropna()