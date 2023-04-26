from fmp_python.fmp import FMP          # for financial API:  pip install fmp-python
import smtplib                          # for sending emails
from email.message import EmailMessage  # for sending emails

from dash import Dash, dcc, html, Output, Input, State      # pip install dash
import plotly.express as px
import pandas as pd                                         # pip install pandas
from datetime import datetime

ticker_list = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Dash_More_Advanced_Shit/Email_Alerts/technology_stocks.csv')


def send_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'p.jain161202@gmail.com'
    msg['from'] = user
    password = 'gwjcotngvyepqrmq'

    # set server parameters
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Stock Market Alert System (Email and SMS)", style={'textAlign': 'center'}),
    html.H2('Made For Minor Project'),
    html.H5("Still in Testing Phase"),
    html.H5("Developed by Prasuk Jain"),
    dcc.Interval(id='trigger', interval=1000*100), # 100 seconds
    dcc.Dropdown(id='ticker-name', options=ticker_list['Ticker'], value='TSLA', clearable=False, style={'width': '50%'}),
    html.Div(id='price-placeholder', children=[]),
    dcc.Graph(id='line-history', figure={}),
    html.Hr(),

    html.Div('Would you like to set up email or phone alerts for price changes?'),
    dcc.RadioItems(id='alert-permission', options=['No','Yes, email alerts', 'Yes, phone alerts'], value='No'),
    html.Div('Alert me when share price is equal or above:'),
    dcc.Input(id='alert-value', type='number', min=0, max=1000, value=0),
])


@app.callback(
    Output('line-history', 'figure'),
    Output('price-placeholder', 'children'),
    Input('trigger', 'n_intervals'),
    Input('ticker-name', 'value'),
    State('alert-permission', 'value'),
    State('alert-value', 'value'),
)
def display_price(_, ticker_name, alert_permission, alert_value):
    fmp = FMP(output_format='pandas', api_key='27521e4850e08bbeb0e1be202b7b6670')
    stock = fmp.get_quote_short(ticker_name)
    stock_history = fmp.get_historical_chart('1hour', ticker_name)
    current_time = datetime.now().strftime("%H:%M:%S")

    if alert_permission == 'Yes, phone alerts':
        if stock.price[0] >= alert_value:
            send_alert('Alert: Buy Stock',
                        f'{ticker_name} passed your alert threshold of ${alert_value} '
                        f'and is now at ${stock.price[0]} per share.',
                        '8819855540')

    elif alert_permission == 'Yes, email alerts':
        if stock.price[0] >= alert_value:
            send_alert('Alert: Buy Stock',
                        f'{ticker_name} passed your alert threshold of ${alert_value} '
                        f'and is now at ${stock.price[0]} per share.',
                        ['rajputhimanshu0330@gmail.com','aashiverma924@gmail.com'])

    history_fig = px.line(stock_history, x='date', y='high')
    return history_fig, html.Pre(f"Time: {current_time}\nPrice: ${stock.price[0]}")


if __name__ == '__main__':
    app.run()
