import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import requests
from dash.dependencies import Input, Output
import coinmarketcap



taxi_data = requests.get('https://api.data.gov.sg/v1/transport/taxi-availability',params=None)

df_train_station = pd.read_csv('mrtsg.csv',sep=',')





df = pd.DataFrame(taxi_data.json()['features'][0]['geometry']['coordinates'][:])
px.set_mapbox_access_token(open("token.mapbox_token").read())
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
fig = px.scatter_mapbox(df,lat=1,lon=0,height=1000,zoom=10,title="Singapore Taxi Data")

fig_train = px.scatter_mapbox(df_train_station,lat='Latitude',lon='Longitude',height=1000,zoom=10,title="Singapore Train data",hover_name='STN_NAME',hover_data=['STN_NAME'])



coin_data = coinmarketcap.coinmarketcapdata()

fig_coin = px.scatter(coin_data,x='id',y='Percentage_Change',range_y=[-1000,1000],hover_name="Coin_ID",hover_data=["Coin_ID"],title="Coin Data")

picker_style = {'float': 'left', 'margin': 'auto'}
fig.update_layout(font_family="Courier New",
    title_font_family="Times New Roman")
fig_train.update_layout(font_family="Courier New",
    title_font_family="Times New Roman")
fig_coin.update_layout(font_family="Courier New",
    title_font_family="Times New Roman")

app.layout = html.Div(children=[
    html.H1(id='my_heading',children='Dash Practice Project'),



dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Taxi_Availability', 'value': 'taxi'},
            {'label': 'Train_Station', 'value': 'parking'},
            {'label': 'Coin_Data', 'value': 'Percentage'}
        ],
        value='taxi'),

        dcc.Graph(id='my_map',figure=fig)
])

@app.callback(
    Output(component_id='my_map',component_property='figure'),
    [Input('dropdown', 'value')]
)
def click_reaction(dropvalue):
        if dropvalue == 'taxi':

            return fig
        elif dropvalue == 'parking':

            return fig_train
        else:

            return fig_coin

if __name__ == '__main__':
    app.run_server(debug=True)