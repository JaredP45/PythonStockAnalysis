# OHLC Chart

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import loop


# user_year = int(input('Enter a year from the past which will display chart from that date to now\n >> '))


def showChart():
    df = loop.readSP500()

    choice = input('Enter a stock to choose')
    df_stock_choice = loop.chooseStock(choice)

    stock_name = df_stock_choice

    df_stock_choice = df[df['Name'] == df_stock_choice].copy()

    df_stock_choice['date'] = pd.to_datetime(df_stock_choice['date'])

    df_stock_choice = df_stock_choice[df_stock_choice['date'].dt.year > 2016]

    df_stock_choice.reset_index(inplace=True)

    x = np.arange(0, len(df_stock_choice))
    fig, (ax, ax2) = plt.subplots(2, figsize=(12, 8), gridspec_kw={'height_ratios': [4, 1]})

    for idx, val in df_stock_choice.iterrows():
        color = '#2CA453'
        if val['open'] > val['close']: color = '#f04370'

        # high/low lines
        ax.plot([x[idx], x[idx]],
                [val['low'], val['high']],
                color=color)

        # open
        ax.plot([x[idx], x[idx] - 0.1],
                [val['open'], val['open']],
                color=color)
        # close
        ax.plot([x[idx], x[idx] + 0.1],
                [val['close'], val['close']],
                color=color)

    # ticks top plot
    ax2.set_xticks(x[::3])
    ax2.set_xticklabels(df_stock_choice.date.dt.date[::3])
    ax.set_xticks(x, minor=True)

    # labels
    ax.set_ylabel('USD')
    ax2.set_ylabel('Volume')

    # grid
    ax.xaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)
    ax2.set_axisbelow(True)
    ax2.yaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)

    # remove spines
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    # plot volume
    ax2.bar(x, df_stock_choice['volume'], color='lightgrey')

    # get max volume + 10% (mx)
    mx = df_stock_choice['volume'].max() * 1.1

    # define tick locations - 0 to max in 4 steps
    yticks_ax2 = np.arange(0, mx + 1, mx / 4)

    # create labels for ticks. Replace 1.000.000 by 'mi'
    yticks_labels_ax2 = ['{:.2f} mi'.format(i / 1000000) for i in yticks_ax2]
    ax2.yaxis.tick_right()  # move ticks to lef side

    # plot y ticks / skip first and last values (0 and max)
    plt.yticks(yticks_ax2[1:-1], yticks_labels_ax2[1:-1])
    plt.ylim(0, mx)

    # title
    ax.set_title(f'{stock_name} Stock Price\n', loc='left', fontsize=20)
    # plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()
