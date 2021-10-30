import plotly.graph_objs as go
import yfinance as yf


data = yf.download(tickers='TSLA', period='5d',
                   interval='15m', round=True)

print(data)

