# ------------------------------------------------------------------------------------------------------------------------
# - Page 1 - Intro
# https://dash.plot.ly/getting-started

# Visual components in libraries: dash_core_components, dash_html_components. (Can build own in JavaScript/React.js

# Layout is composed of a tree of components, like html.Div and dcc.Graph
# dash_html_components library has a component for every html tag
# html.H1(children='Hello Dash') component generates a <h1>Hello Dash</h1> HTML element
# dash_core_components describe higher-level components that are interactive and are generated with JavaScript, HTML, and CSS through the React.js library

# The children property is special. By convention, it's always the first attribute which means that you can omit it:
# html.H1(children='Hello Dash') is the same as html.H1('Hello Dash'). Also, it can contain a string, a number, a single component, or a list of components.

# For debugging: app.run_server(debug=True)

# Differences between dash_html_components and HTML attributes
# html.H1('Hello Dash', style={'textAlign': 'center', 'color': '#7FDBFF'}) ==  <h1 style="text-align: center; color: #7FDBFF">Hello Dash</h1>.
# Style in HTML is a semicolon separated string - In dash, you just supply a dictionary
# Keys in dictionary are camel cased. (So, instead of text-align, it's textAlign)
# The HTML class attribute is className in Dash
# The children of the HTML tag is specified through the children keyword argument.

# The figure argument in the dash_core_components.Graph component is the same figure argument that is used by plotly.py

# Calling for help: help(dcc.Dropdown)

# * CSS tutorial: https://dash.plot.ly/external-resources
# * Plotly documentations and gallery: https://plot.ly/python/
# * Markdown tutorial: https://commonmark.org/help/
# * Dash core components: https://dash.plot.ly/dash-core-components
# * Dash HTML components: https://dash.plot.ly/dash-html-components

# ------------------------------------------------------------------------------------------------------------------------
# - Page 2 - Making it interactive
# https://dash.plot.ly/getting-started-part-2

# Making it interactive:

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div')
])

# (This works as well) The component_id and component_property keywords are optional (there are only two arguments for each of those objects).
# @app.callback(
#     Output('my-div', 'children'),
#     [Input('my-id', 'value')]
# )
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)

# The "inputs" and "outputs" of our application interface are described declaratively through the app.callback decorator
# In Dash, the inputs and outputs of our application are simply the properties of a particular component.
# In this example, our input is the "value" property of the component that has the ID "my-id".
# Our output is the "children" property of the component with the ID "my-div"
# Whenever an input property changes, the function that the callback decorator wraps will get called automatically

# It's also possible to have multiple input components and chained outputs


# ------------------------------------------------------------------------------------------------------------------------
# - Page 3 - State changes
# https://dash.plot.ly/state

# Check this out for interacting with pages/running callbacks with a submit button instead of reacting

# ------------------------------------------------------------------------------------------------------------------------
# - Page 4 - Interactive Graphing
# https://dash.plot.ly/interactive-graphing

# Check this out for building awesome graphs

# ------------------------------------------------------------------------------------------------------------------------
# - Page 5 - Sharing data between callbacks
# https://dash.plot.ly/sharing-data-between-callbacks

# Three main places to keep data in memory
# 1- In the user's browser session | 2- On the disk (e.g. on a file or on a new database) | 3- In a shared memory space like with Redis
# Run multiple processes: app.run_server(debug=True, processes=6)

# ------------------------------------------------------------------------------------------------------------------------
# - END -











