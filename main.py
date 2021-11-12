from chart import AnalysisChart as Ac

if __name__ == '__main__':
    choice = input("Write a stock symbol: ")

    Ac.showData(Ac(choice))
