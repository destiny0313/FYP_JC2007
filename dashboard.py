# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:49:05 2020

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:35:43 2020
@author: user
"""

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output
import yfinance as yf
import os

filepath = os.path.abspath(os.getcwd())+"\\Source\\Stock_List.csv"

df = pd.read_csv(filepath, index_col=(False))

def create_line_graph(df):

    name=""
    data = {}
    for stock in df['Ticket']:
        data[stock] = yf.download(stock,period='max')
        name = str(stock)
        
    fig = px.line(x=data[name].index, y=data[name].Close, labels={'x':'Date', 'y':'Closing Price'},title=name+" Historical Closing Price")
    return fig

title = {
    'font-family': 'Poppins',
    'font-weight': 'bold',
    'font-size': '4em'
}
card = {
    'border-radius': '1em',
    'border': 0,
    'box-shadow': '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 10px 0 rgba(0, 0, 0, 0.19)',
    'color': 'black',
    'font-family': 'Open Sans',
    "padding": "5px"
}
row = {
    'margin-bottom':'2em',
}
cell = {
    "padding": "5px",
    "textAlign": "center",
    'color': 'black'
}
header = {
    "backgroundColor": "rgb(230, 230, 230)",
    "fontWeight": "bold",
}
dashboard = {
    'background': '#232946', 
    'padding': '2em 8em 2em 8em', 
    'color': 'white'
}
col = {
       'width' : '33%'
}


external_stylesheets = ["https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Poppins:wght@400;500;700&display=swap", dbc.themes.BOOTSTRAP]
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

title_component = html.Div(html.H1("📈 FYP JC2007 Dashboard (2020-2021)", style=title))
line_graph = dcc.Graph(id='line-graph')
line_card = dbc.Card(line_graph, style=card)
something_here = html.Div(html.H1("Here is a test", style=title))

stockSlider = dcc.Slider(
    id='stock-slider-Net-Income-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider2 = dcc.Slider(
    id='stock-slider-Operating-Income-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider3 = dcc.Slider(
    id='stock-slider-PE-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider4 = dcc.Slider(
    id='stock-slider-EPS',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider5 = dcc.Slider(
    id='stock-slider-Working-Capital',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider6 = dcc.Slider(
    id='stock-slider-ROE',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider7 = dcc.Slider(
    id='stock-slider-PE',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider8 = dcc.Slider(
    id='stock-slider-PB',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider9 = dcc.Slider(
    id='stock-slider-Current-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider10 = dcc.Slider(
    id='stock-slider-Debt-To-Equity',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider11 = dcc.Slider(
    id='stock-slider-Debt-To-Asset',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider12 = dcc.Slider(
    id='stock-slider-Dividend-Yield',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider13 = dcc.Slider(
    id='stock-slider-Market-Capital',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.5,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )


stockDropdown = dcc.Dropdown(
    id='stock-dropdown', 
    options=[{'label': data, 'value': data} for data in df['Ticket']], 
    multi=False, 
    searchable=True,
    value=['AAPL']
)

slider_card = dbc.Card([dbc.Row([dbc.Col([html.P("Net Income Ratio:"), html.Div(stockSlider)],style=col), 
                                 dbc.Col([html.P("Operating Income Ratio:"), html.Div(stockSlider2)],style=col)]),
                        dbc.Row([dbc.Col([html.P("Gross Profit Ratio:"), html.Div(stockSlider3)],style=col), dbc.Col([html.P("EPS"), html.Div(stockSlider4)],style=col)]),
                        dbc.Row([dbc.Col([html.P("Working Capital:"), html.Div(stockSlider5)],style=col), dbc.Col([html.P("ROE:"), html.Div(stockSlider6)],style=col)]),
                        dbc.Row([dbc.Col([html.P("P/E Ratio:"), html.Div(stockSlider7)],style=col), dbc.Col([html.P("P/B Ratio:"), html.Div(stockSlider8)],style=col)]),
                        dbc.Row([dbc.Col([html.P("Current Ratio:"), html.Div(stockSlider9)],style=col), dbc.Col([html.P("Debt-To-Equity:"), html.Div(stockSlider10)],style=col)]),
                        dbc.Row([dbc.Col([html.P("Debt-To-Assets:"), html.Div(stockSlider11)],style=col), dbc.Col([html.P("Dividend Yield:"), html.Div(stockSlider12)],style=col)]),
                        dbc.Row([dbc.Col([html.P("Market Capital:"), html.Div(stockSlider13)],style=col), dbc.Col([], style=col)])],style=card)

widget_card = dbc.Card([
                    html.Div(stockDropdown)
                    ], style=card)

def get_filtered_df(df, stocks):
    filtered_df = df[(df['Ticket'].isin([stocks]))]
    
    return filtered_df

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(title_component),
            justify="center",
            align="center",
            className="text-center",
            style=row
        ),        
        dbc.Row(widget_card, style=row),   
        dbc.Row([dbc.Col(line_card)], style=row),
        slider_card
    ],
    style=dashboard,
    fluid = True,
)
app.layout = layout

@app.callback(
    Output('line-graph', 'figure'),
    [
        Input('stock-dropdown', 'value'),
    ])
def update_figure(stocks):

    if stocks is None : stocks = ['AAPL']
    filtered_df = get_filtered_df(df, stocks)
    
    line_fig = create_line_graph(filtered_df)
    line_fig.update_layout()
    
    return line_fig

@app.callback(
    Output('a'),
    [
     Input('stock-slider-EPS','value'),
     Input('','value')]
    )
def test(hi):
    return 1

app.run_server( port=8000)