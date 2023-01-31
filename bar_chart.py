import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from util import get_olympic_data
from ids import *

def render(app):
    df = get_olympic_data()  

    @app.callback(
        Output(component_id=BAR, component_property='children'),
        Input(component_id=COUNTRIES, component_property='value'),
    )

    def update_bar_chart(countries):
        filtered_data = df.query("Team in @countries")
        if filtered_data.shape[0]==0:
            return html.Div(children=[
                dbc.Alert("No Countries selected", color="danger")
                ],id=BAR)
        fig = px.bar(filtered_data, x='Medal', y='Count', orientation='v',color = 'Team',title = "Top 20 Olympic Medals by Country")
        return html.Div(dcc.Graph(figure=fig),id=BAR)
    return html.Div(id=BAR)