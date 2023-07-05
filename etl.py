import requests
import datetime
import pandas as pd

# Extract data from API


def Extract(days=1):
    date = datetime.datetime.today() - datetime.timedelta(days=1)
    params = {'date': date.strftime('%Y-%m-%d')}
    response = requests.get(
        "https://api.data.gov.sg/v1/environment/4-day-weather-forecast", params=params)

    date_list, forecast_list, temp_high_list, temp_low_list = [], [], [], []
    for i in range(4):
        date_list.append(response.json()['items'][0]['forecasts'][i]['date'])
        forecast_list.append(
            response.json()['items'][0]['forecasts'][i]['forecast'])
        temp_high_list.append(
            response.json()['items'][0]['forecasts'][i]['temperature']['high'])
        temp_low_list.append(
            response.json()['items'][0]['forecasts'][i]['temperature']['low'])

    df = pd.DataFrame({'Date': date_list, 'Forecast': forecast_list,
                      'Temp_High': temp_high_list, 'Temp_Low': temp_low_list})

    print(df)
    return df

# Transform data


def Transform(df):
    df['Date'] = pd.to_datetime(df['Date'])

    return df


def ETL():
    df = Extract()
    df = Transform(df)


ETL()
