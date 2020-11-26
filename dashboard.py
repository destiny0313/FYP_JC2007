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

filepath_ranking = os.path.abspath(os.getcwd())+"\\Source\\attribute_ranking.csv"
df_ranking = pd.read_csv(filepath_ranking, index_col=(False))

def ranking(a,b,c,d,e,f,g,h,i,j,k,l,m):
    rank_result = {}
    final_rank = []
    for each, content in df_ranking.iterrows():
        rank_result[content['Unnamed: 0']] = content['Net_Income_Ratio_Ranking']*a+content['Operating_Income_Ratio_Ranking']*b+content['Gross_Profit_Ratio_Ranking']*c+content['EPS_Ranking']*d+content['Working_Capital_Ranking']*e+content['ROE_Ranking']*f+content['PE_Ratio_Ranking']*g+content['PB_Ratio_Ranking']*h+content['Current_Ratio_Ranking']*i+content['Debt_To_Equity_Ranking']*j+content['Debt_To_Asset_Ranking']*k+content['Dividend_Yield_Ranking']*l+content['Market_Capital_Ranking']*m
        #rank_result[content['Unnamed: 0']] = content['Net_Income_Ratio_Ranking']*a
    for i in range(10):
        tmp = min(rank_result.keys(), key = (lambda k: rank_result[k]))
        final_rank.append(tmp)
        rank_result.pop(tmp)
    return final_rank


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
    'width' : '50%'
}
result_header = {
    'font-family': 'Poppins',
    'font-weight': 'bold',
    'font-size': '2em'
}
result_subhead = {
    'font-family': 'Poppins',
    'font-size': '1em'
}



external_stylesheets = ["https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Poppins:wght@400;500;700&display=swap", dbc.themes.BOOTSTRAP]
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

title_component = html.Div(html.H1("📈 FYP JC2007 Dashboard (2020-2021)", style=title))
line_graph = dcc.Graph(id='line-graph')
line_card = dbc.Card(line_graph, style=card)
fundamental_ranking_result = dbc.Card([
    dbc.Row([html.P("Result", style=result_header)], justify = "center", align = "center"),
    dbc.Row([html.P("1st: ", style=result_subhead), html.P("",id="1st_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("2nd: ", style=result_subhead), html.P("",id="2nd_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("3rd: ", style=result_subhead), html.P("",id="3rd_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("4th: ", style=result_subhead), html.P("",id="4th_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("5th: ", style=result_subhead), html.P("",id="5th_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("6th: ", style=result_subhead), html.P("",id="6th_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("7th: ", style=result_subhead), html.P("",id="7th_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("8th: ", style=result_subhead), html.P("",id="8th_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("9th: ", style=result_subhead), html.P("",id="9th_rank", style=result_subhead)], justify = "center", align = "center", style=row),
    dbc.Row([html.P("10th: ", style=result_subhead), html.P("",id="10th_rank", style=result_subhead)], justify = "center", align = "center", style=row)],style=card)

stockSlider = dcc.Slider(
    id='stock-slider-Net-Income-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.7,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider2 = dcc.Slider(
    id='stock-slider-Operating-Income-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.7,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider3 = dcc.Slider(
    id='stock-slider-Gross-Profit-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 1,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider4 = dcc.Slider(
    id='stock-slider-EPS',
    min = 0,
    max = 1,
    step = 0.1,
    value = 1,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider5 = dcc.Slider(
    id='stock-slider-Working-Capital',
    min = 0,
    max = 1,
    step = 0.1,
    value = 1,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )

stockSlider6 = dcc.Slider(
    id='stock-slider-ROE',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.8,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider7 = dcc.Slider(
    id='stock-slider-PE',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider8 = dcc.Slider(
    id='stock-slider-PB',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider9 = dcc.Slider(
    id='stock-slider-Current-Ratio',
    min = 0,
    max = 1,
    step = 0.1,
    value = 1.0,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider10 = dcc.Slider(
    id='stock-slider-Debt-To-Equity',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.8,
    marks = {0:"0.0",0.1:"0.1",0.2:"0.2",0.3:"0.3",0.4:"0.4",0.5:"0.5",0.6:"0.6",0.7:"0.7",0.8:"0.8",0.9:"0.9",1:"1.0"}
    )
stockSlider11 = dcc.Slider(
    id='stock-slider-Debt-To-Asset',
    min = 0,
    max = 1,
    step = 0.1,
    value = 0.8,
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
    value = 1,
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
        dbc.Row([dbc.Col(slider_card, style=col), dbc.Col(fundamental_ranking_result, style=col)],style=row)
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
    [
     Output('1st_rank','children'),
     Output('2nd_rank','children'),
     Output('3rd_rank','children'),
     Output('4th_rank','children'),
     Output('5th_rank','children'),
     Output('6th_rank','children'),
     Output('7th_rank','children'),
     Output('8th_rank','children'),
     Output('9th_rank','children'),
     Output('10th_rank','children')],
    [
     Input('stock-slider-Net-Income-Ratio','value'),
     Input('stock-slider-Operating-Income-Ratio','value'),
     Input('stock-slider-Gross-Profit-Ratio','value'),
     Input('stock-slider-EPS','value'),
     Input('stock-slider-Working-Capital','value'),
     Input('stock-slider-ROE','value'),
     Input('stock-slider-PE','value'),
     Input('stock-slider-PB','value'),
     Input('stock-slider-Current-Ratio','value'),
     Input('stock-slider-Debt-To-Equity','value'),
     Input('stock-slider-Debt-To-Asset','value'),
     Input('stock-slider-Dividend-Yield','value'),
     Input('stock-slider-Market-Capital','value'),]
    )
def test(a,b,c,d,e,f,g,h,i,j,k,l,m):
    rank = []
    rank = ranking(a,b,c,d,e,f,g,h,i,j,k,l,m)
    return rank[0],rank[1],rank[2],rank[3],rank[4],rank[5],rank[6],rank[7],rank[8],rank[9]

app.run_server( port=8000)