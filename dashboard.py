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
    'margin-bottom':'2em'
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


external_stylesheets = ["https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Poppins:wght@400;500;700&display=swap", dbc.themes.BOOTSTRAP]
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

title_component = html.Div(html.H1("📈 FYP JC2007 Dashboard (2020-2021)", style=title))
line_graph = dcc.Graph(id='line-graph')
line_card = dbc.Card(line_graph, style=card)
something_here = html.Div(html.H1("Here is a test", style=title))



stockDropdown = dcc.Dropdown(
    id='stock-dropdown', 
    options=[{'label': data, 'value': data} for data in df['Ticket']], 
    multi=False, 
    searchable=True,
    value=['AAPL']
)

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
        dbc.Row([dbc.Col(line_card),dbc.Col(something_here)], style=row),
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

app.run_server( port=8000)