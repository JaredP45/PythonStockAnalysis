import plotly.graph_objs as go
import yfinance as yf


data = yf.download(tickers='TSLA', period='5d',
                   interval='15m', round=True)

fig = go.figure()

fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'],
                             low=data['Low'], close=data['Close'], name='market data'))

fig.update_layout(title='Tesla Share Price', yaxis_title='Stock Price (USD)')



