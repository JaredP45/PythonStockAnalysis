from chart import AnalysisChart as Ac

if __name__ == '__main__':
    choice = input("Write a stock symbol: ")
    charting_style = int(input('Do you want OHLC or Candlestick charting? (1/2)\n>>> '))

    Ac.showData(Ac(choice, charting_style))
