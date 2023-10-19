import dash
# import dash_html_components as html
from dash import html
import base64
from flask import Flask, Response
import os
import dash_daq as daq
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.io as pio
import dash_bootstrap_components as dbc
# import dash_core_components as dcc
from dash import dcc


server = Flask(__name__)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], server=server)
# app.config['suppress_callback_exceptions'] = True

# interval = dcc.Interval(
#     id='interval-component',
#     interval=1000, # in milliseconds
#     n_intervals=0
# )



# theme = {
#     'dark': True,
#     'detail': '#007439',
#     'primary': '#00EA64',
#     'secondary': '#6E6E6E',
# }

# colors = {
#         'backgroundColor': '#111111',
#         'text': '#7FDBFF'
#     }

# def get_video_files():
#     vid_files = os.listdir('/Users/skattish/Documents/image_process/static/videos/')
#     video_formats = {'mov', 'mp4'}
#     complete = set()
#     trace = []
#     print('here')
#     for i, vid in enumerate(vid_files):
#         if vid.split('.')[-1] in video_formats and vid not in complete:
#             trace.append(
#                 html.Img(id = str(vid) + '_' + str(i),
#                          src = '/static/images/test_img.jpg',
#                          n_clicks = 0,
#                          style = {
#                             'height':'200px',
#                             'width':'300px',
#                             'padding':'30px'
#                          }
#                          )
#                 )
#     return trace

# def index_page():
#     return html.Div(get_video_files())

# default_layout = html.Div(
#         [html.H1('Main Page'),
#                 html.Div(id = 'main', children = 
#                     [
#                     dcc.Interval(
#                         id='interval-component',
#                         interval=1000, # in milliseconds
#                         n_intervals=0
#                     ),
#                     html.Div(id = 'main_layout', children = [
#                     # daq.DarkThemeProvider(theme=theme, children = [
#                         html.H1('Smart Learn',                                            #Headline
#                                 style = {
#                                 'textAlign': 'center',
#                                 'color': colors['text'],
#                                 # 'position':'fixed',
#                                 'float':'center'
#                                 }
#                                 ),
        
#                         html.Hr(),
        
#                         index_page(),
#                         html.Div(id = 'img_populate'),
#                         html.Div(id = 'video_populate'),
        
#                         html.H3('copyrights',                                            #Headline
#                                 style = {
#                                 'position': 'fixed',
#                                 'height': '50px',
#                                 # 'background'-color: red;
#                                 'bottom': '0px',
#                                 'left': '0px',
#                                 'right': '0px',
#                                 'margin-bottom': '0px',
#                                 }
#                                 )
#                         ]),
                        
#                         ],
#                 )]

#     )

# def serve_layout(layout = None):
#     if layout == None:
#         return default_layout
#     else:
#         return layout

# app.layout = serve_layout



# @app.callback(Output('img_populate', 'children'),
#               [Input('interval-component', 'n_intervals')])
# def update_metrics(n):
#     component = html.Div(get_video_files()) # create new children for some-output-component
#     return component

# @app.callback(Output('img_populate', 'style'),
#               [Input('img1', 'n_clicks')])
# def update_l(clicks):
#     if clicks%2 == 0:
#         return {'display': 'block'}
#     else:
#         return {'display': 'none'}

# @app.callback(dash.dependencies.Output('video_populate', 'children'),
#              [dash.dependencies.Input('img1', 'n_clicks')])
# def toggle_container(clicks):
#     if clicks%2 != 0:
#         return html.Video(
#             controls = True,
#             id = 'movie_player',
#             src = "/static/videos/test_vid.mov",
#             # src = "https://www.w3schools.com/html/mov_bbb.mp4",
#             autoPlay=False,
#             width = 600,
#             title = 'pre-loaded video demo'
#         )

@server.route('/')
def home():
    return 'you are in the home page'

@server.route('/static/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(os.path.join(root_dir, 'static'), path)


if __name__ == '__main__':
    server.run(debug=True)









