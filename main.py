from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from pages import graficos, formulario
from app import app
import os
from app import app


navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
    ],
    brand="DashTitanic",
    brand_href="#",
    color="primary",
    dark=True
)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    navegacao,
    html.Div(id="page-content")
])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def abre_pagina(pathname):
    if pathname == "/formulario":
        return formulario.layout
    elif pathname == "/graficos":
        return graficos.layout
    else:
        return html.P("Página Inicial")
    

port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port, debug=False)