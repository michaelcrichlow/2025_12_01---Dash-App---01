# imports
import os
from dash import Dash, html
from dash import dcc, Input, Output, State # new imports

# create the app and server
app = Dash(__name__)
server = app.server

# layout
app.layout = html.Div([
    html.H1("Goal Tracker Dashboard - Day 01"),
    html.P("Type a goal below:"),

    # two new lines
    dcc.Input(id="goal-input", type="text", placeholder="Type something..."),
    html.Div(id="goal-output", style={"marginTop": "20px", "fontWeight":"bold"}),
    html.Hr(),

    html.P("Type something else below:"),
    dcc.Input(id="input-001", type="text", placeholder="Type, click Submit..."),
    html.Button("Submit", id="submit-btn"),
    html.Div(id="output-002", style={"marginTop": "20px", "fontWeight":"bold"})
])


# Callback for first input box
# Oh! This is a decorator for the `update_output` function! (didn't realize that at first)
# `update_function()` doesn't have to be called that. This is just a name that makes sense.
@app.callback(
    Output("goal-output", "children"),
    Input("goal-input", "value"),
)
def update_output(value) -> str:
    if value:
        return f"See how this updates in real time: {value}"
    return "Nothing entered yet."


# Callback for second input box
@app.callback(
    Output("output-002", "children"),
    [Input("input-001", "n_submit"),Input("submit-btn", "n_clicks")],
    State("input-001", "value"),
)
def another_function(n_submit, n_clicks, value) -> str:
    if (n_submit or n_clicks) and value:
        return f"This updates when you press `Enter` or click `Submit`: {value}"
    return "Nothing entered yet."

# entry point
if __name__ == "__main__":
    #port
    port = int(os.environ.get("PORT", 8050))
    
    # app.run()
    app.run(host="0.0.0.0" , port=port, debug=False)
