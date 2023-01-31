import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from util import get_olympic_data
from ids import *

def render(app):
    df = get_olympic_data() 
    all_countries = df["Team"].unique()
    return html.Div(
        [
            dbc.Label("Select Countries"),
            dbc.Checklist(
                id=COUNTRIES_CHECK,
                options=[{"label": i, "value": i} for i in all_countries],
                value = all_countries,
                inline=True,
            ),
        ],
        className="mb-4",
    )