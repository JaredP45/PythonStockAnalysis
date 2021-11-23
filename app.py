import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('data/SP500/all_stocks_5yr.csv')
df.index = pd.to_datetime(df['date'])

col = df.loc[:, 'open':'close']
df['stock_mean'] = col.mean(axis=1)

app = dash.Dash(__name__)


# Creates a list of dictionaries, which have the keys 'label' and 'value'.
def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})
    return dict_list


app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('JPaubel - Stock Analysis Tool'),
                                  html.P('Python with Data Science Final Project'),
                                  html.P('Pick one or more stocks from the dropdown below.'),
                                  html.Div(className='div-for-dropdown',
                                           children=[
                                               dcc.Dropdown(id='stockselector',
                                                            options=get_options(df['Name'].unique()),
                                                            multi=True,
                                                            value=[df['Name'].sort_values()[0]],
                                                            style={'backgroundColor': '#2e3440'},
                                                            className='stockselector')
                                           ],
                                           style={'color': '#2e3440'})
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-light-grey',
                              children=[
                                  dcc.Graph(id='timeseries',
                                            config={'displayModeBar': False},
                                            animate=True),
                                  dcc.Graph(id='change', config={'displayModeBar': False})
                              ]
                              )
                 ]
                 )
    ]
)


@app.callback(Output('timeseries', 'figure'),
              [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):
    """ Draw traces of the feature 'value' based one the currently selected stocks """
    trace = []
    df_sub = df
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['Name'] == stock].index,
                                y=df_sub[df_sub['Name'] == stock]['stock_mean'],
                                mode='lines',
                                opacity=0.7,
                                name=stock,
                                textposition='bottom center'))

    traces = [trace]
    data = [val for sublist in traces for val in sublist]

    figure = {'data': data,
              'layout': go.Layout(
                  colorway=['#DF2935', '#679436', '#FF6542', '#427AA1', '#2D0320', '#064789'],
                  template='plotly_dark',
                  paper_bgcolor='#2A3850',
                  plot_bgcolor='#eceff4',
                  margin={'b': 15},
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Stock Prices', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                  yaxis_title={'text': 'Share Price'},
                  xaxis_title={'text': 'Date Range'},
              ),
              }
    return figure


@app.callback(Output('change', 'figure'),
              [Input('stockselector', 'value')])
def update_change(selected_dropdown_value):
    """ Draw traces of the feature 'change' based one the currently selected stocks """

    trace = []
    df_sub = df
    for stock in selected_dropdown_value:
        trace.append(go.Scatter(x=df_sub[df_sub['Name'] == stock].index,
                                y=df_sub[df_sub['Name'] == stock]['volume'],
                                mode='lines',
                                opacity=0.7,
                                name=stock,
                                textposition='bottom center'))
    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    figure = {'data': data,
              'layout': go.Layout(
                  colorway=['#DF2935', '#679436', '#FF6542', '#427AA1', '#2D0320', '#064789'],
                  template='plotly_dark',
                  paper_bgcolor='#2A3850',
                  plot_bgcolor='#eceff4',
                  margin={'t': 50},
                  height=250,
                  hovermode='x',
                  autosize=True,
                  title={'text': 'Market Volume', 'font': {'color': 'white'}, 'x': 0.5},
                  xaxis={'range': [df_sub.index.min(), df_sub.index.max()]},
                  yaxis_title={'text': 'Volume in Million'},
                  xaxis_title={'text': 'Date Range'},
              ),
              }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
