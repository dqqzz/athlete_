from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import pandas as pd
from util import get_countries
from ids import *


def render(app):
    list_countries = get_countries()
    all_countries = [{'label':i,'value':i} for i in list_countries]
    @app.callback(
    Output(component_id=COUNTRIES, component_property='value'),
    Input(component_id=SELECT_BOTTON, component_property='n_clicks')
    )
    def update_all_countries(n):
        return list_countries


    return html.Div(
        children=[
            html.H6("Select country"),
            dcc.Dropdown(
                options = all_countries,
                multi=True,
                id = COUNTRIES,
                value = "United States"
            ),
            dbc.Button(
                children=["Select all"], 
                color="primary", 
                className="me-1",
                id=SELECT_BOTTON,
                n_clicks=0
            )
        ]
    )