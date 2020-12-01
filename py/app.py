import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
#import mysql.connector

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

my_sql_connector = "mysql+pymysql://pc2labfinal:password@mysqldata/classicmodels"
engine = create_engine(my_sql_connector)
df = pd.read_sql_table("customers", engine)

server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

# connection = mysql.connector.connect(user='pc2labfinal', password='password', host='192.168.160.2', database='pc2labfinal')

Graf1 = px.histogram(df, x="country", title='Distribution by Country')
Graf2 = px.scatter(df, y="salesRepEmployeeNumber", x="creditLimit", color="customerName", title='Sales Representation and Credit Limit Relation')
Graf3 = px.box(df, x="creditLimit", title="Average Credit Limit", points="all")

app.layout = html.Div(texto=[
    html.H1("Dash PC2 aplication"),

    html.Div(texto="Juan Pablo Useche y Manuel Rodriguez"),

    dcc.Graph(
        id='Grafico1',
        Grafico1=Graf1),

    dcc.Graph(
        id='Grafico2',
        Grafico2=Graf2),
        
    dcc.Graph(
        id='Grafico3',
        Grafico3=Graf3),
])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True, port=8050)