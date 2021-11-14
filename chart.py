import plotly.graph_objs as go
import yfinance as yf


class AnalysisChart:
    def __init__(self, choice='', charting=1):
        self.choice = choice.upper()
        self.charting = charting

    def showData(self):
        """
        Loads the data for a period of 1 year, then sets the figure and traces based on which is chosen. Then it sets
            the title ticks, and shows the entire chart.
        """

        data = yf.download(tickers=self.choice, period='360d',
                           rounding=True)

        fig = go.Figure()

        if self.charting == 1:
            fig.add_trace(go.Ohlc(x=data.index, open=data['Open'], high=data['High'],
                                  low=data['Low'], close=data['Close'], name='market data'))
        elif self.charting == 2:
            fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data['High'],
                                         low=data['Low'], close=data['Close'], name='market data'))
        else:
            print('Charting option does not exist.')

        fig.update_layout(title=self.choice + ' Share Price', yaxis_title='Stock Price (USD)')

        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=5, label='5 Days', step='day', stepmode='backward'),
                    dict(count=15, label='15 Days', step='day', stepmode='backward'),
                    dict(count=30, label='1 Month', step='day', stepmode='backward'),
                    dict(count=60, label='2 Months', step='day', stepmode='backward'),
                    dict(step='all')
                ])
            )
        )

        fig.show()
