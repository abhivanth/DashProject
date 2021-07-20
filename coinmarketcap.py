from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd



def coinmarketcapdata():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '2116947d-5a25-4d9c-8840-f17a61464279',
    }

    session = Session()
    session.headers.update(headers)
    coin_dataframe = pd.DataFrame(columns=['id','Percentage_Change', 'Coin_ID', 'Coin_Name'])

    try:
        response = session.get(url, params=parameters)
        response = response.json()

        # print(response['data'][0]['quote']['USD']['percent_change_90d'])

        for id in range(5000):
            coin_dataframe = coin_dataframe.append(
                {'id':id,'Percentage_Change': response['data'][id]['quote']['USD']['percent_change_90d'],
                 'Coin_ID': response['data'][id]['symbol'], 'Coin_Name': response['data'][id]['name']},
                ignore_index=True)



    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    return coin_dataframe

