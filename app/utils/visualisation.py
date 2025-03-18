import plotly.graph_objects as go

def generate_candlestick(data, title, x_label, y_label):
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])
                        ])
    return fig.to_json()