from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeChangerAIO
import bar_chart, countries,checklist

def create_layout(app):
    header = html.H1("The Olympics")
    return dbc.Container(children = [
        header,
        dbc.Row(
            [
                dbc.Col([
                    countries.render(app),
                    checklist.render(app),
                    # ThemeChangerAIO(aio_id="theme"),
                ], width=4),
                dbc.Col([bar_chart.render(app),], width=8)
            ]
        )
   ],fluid=True,className="dbc")