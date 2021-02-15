from flask import Blueprint, render_template, current_app
from stock_app.stock_data import fetch_income, fetch_price

stock = Blueprint('stock', __name__)


@stock.route("/<string:ticker>")
def quote(ticker):
    price = fetch_price(ticker, current_app.config)
    # return f"The Price of {ticker} is {price}".format(ticker=ticker, price=price)
    return render_template('stock/quote.html', ticker=ticker, stock_price=price)


@stock.route('/<string:ticker>/financials')
def financials(ticker):
    data = fetch_income(ticker, current_app.config)

    chart_data = [float(q["EPS"]) for q in data if q["EPS"]]
    chart_params = {"type": 'line',
                    "data": {
                        'labels': [q["date"] for q in data if q["EPS"]],
                        'datasets': [{'label': 'EPS', 'data': chart_data}]
                    }}
    return render_template('stock/financials.html', ticker=ticker, financials=data, chart_params=chart_params)
