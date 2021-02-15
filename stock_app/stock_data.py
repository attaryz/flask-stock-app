import requests

API_URL = '{base_url}/stock/real-time-price/{ticker}'


def fetch_price(ticker, config):
    data = requests.get(API_URL.format(base_url=config['STOCK_API_BASE_URL'],
                                       ticker=ticker.upper()),
                        params={'apikey': config['STOCK_API_KEY']}).json()
    return data["price"]


def fetch_income(ticker, config):
    url = '{}/financials/income-statement/{}'.format(config['STOCK_API_BASE_URL'], ticker)
    api_params = {'period': 'quarter', 'apikey': config['STOCK_API_KEY']}
    financials = requests.get(url, params=api_params).json()["financials"]
    financials.sort(key=lambda quarter: quarter['date'])
    return financials
