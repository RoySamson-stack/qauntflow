import plotly.graph_objects as go

def generate_candlestick(data):
    """
    Generate a candlestick chart from financial data.
    
    Args:
        data (dict): Financial data in dictionary format.
    
    Returns:
        str: A JSON representation of the candlestick chart.
    """
    df = pd.DataFrame(data)

    fig = go.Figure(data=[go.Candlestick(
        x=df['date'],
        open=df['open'],
        high=df['high'],
        low=df['low'],
        close=df['close']
    )])

    return fig.to_json()