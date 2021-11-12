import plotly.graph_objs as go
import yfinance as yf


class AnalysisChart:
    def __init__(self, choice=''):
        self.choice = choice.upper()

    def showData(self):

        data = yf.download(tickers=self.choice, period='30d',
                           rounding=True)

        fig = go.Figure()

        fig.add_trace(go.Ohlc(x=data.index, open=data['Open'], high=data['High'],
                                     low=data['Low'], close=data['Close'], name='market data'))

        fig.update_layout(title=self.choice + ' Share Price', yaxis_title='Stock Price (USD)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=60, label='60h', step='hour', stepmode='backward'),
                    dict(count=120, label='120h', step='hour', stepmode='backward'),
                    dict(count=480, label='480h', step='hour', stepmode='backward'),
                    dict(count=720, label='720h', step='hour', stepmode='backward'),
                    dict(step='all')
                ])
            )
        )

        fig.show()
