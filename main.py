from chart import AnalysisChart as Ac

if __name__ == '__main__':
    end_program = False

    while end_program is not True:

        choice = input("Write a stock symbol: ")
        charting_style = int(input('Do you want OHLC or Candlestick charting? (1/2)\n>>> '))

        Ac.showData(Ac(choice, charting_style))

        option = input('Do you want to change stocks? (Y/N)\n>>> ')

        if option[0] == 'Y' or option[0] == 'y':
            end_program = False
        elif option[0] == 'N' or option[0] == 'n':
            end_program = True
        else:
            print('An error has occurred.')
            end_program = True
