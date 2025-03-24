import plotly.graph_objects as go
import pandas as pd
import json

def generate_chart(df, chart_type='candlestick'):
    """Generate interactive chart using Plotly"""
    if chart_type == 'candlestick':
        fig = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close'],
            name='Price'
        )])
    else:
        fig = go.Figure(data=[go.Scatter(
            x=df.index,
            y=df['close'],
            name='Price'
        )])
    
    # Add moving averages if they exist
    if 'sma_20' in df.columns:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['sma_20'],
            name='SMA 20',
            line=dict(color='orange', width=1)
        ))
    
    if 'sma_50' in df.columns:
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df['sma_50'],
            name='SMA 50',
            line=dict(color='blue', width=1)
        ))
    
    fig.update_layout(
        xaxis_rangeslider_visible=False,
        height=600,
        title='Price Chart with Indicators'
    )
    
    return json.loads(fig.to_json())