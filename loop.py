import pandas as pd


def readSP500():
    df = pd.read_csv('SP500/all_stocks_5yr.csv')
    return df


def checkIfInSP500():
    stock_list = []

    for stock in readSP500()['Name']:
        if stock not in stock_list:
            stock_list.append(stock)

    return stock_list


def showSP500Options():
    print(checkIfInSP500())


def chooseStock(choice):
    accepted = ''
    rejected = ''
    is_in_sp500 = True

    while is_in_sp500:
        choice = choice.upper()

        if choice in checkIfInSP500():
            accepted = choice
            is_in_sp500 = False
        else:
            print('Chosen stock is not in S&P 500.')
            choice = input()
            continue

    return accepted
