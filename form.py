from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.Label("Peso (kg):"),
    dcc.Input(id="peso", type="number", value=0),
    
    html.Label("Altura (m):"),
    dcc.Input(id="altura", type="number", value=0),
    
    html.Button("Calcular IMC", id="btn-calcular", n_clicks=0),
    
    html.Div(id="output-imc")
])

@app.callback(
    Output("output-imc", "children"),
    Input("btn-calcular", "n_clicks"),
    State("peso", "value"),
    State("altura", "value"),
    prevent_initial_call=True
)
def calcula_imc(n_clicks, peso, altura):
    if n_clicks == 0 or peso is None or altura is None or altura <= 0:
        return ""
    imc = peso / (altura ** 2)
    return f"O seu IMC é: {imc:.2f}"
        
app.run_server(debug=True)