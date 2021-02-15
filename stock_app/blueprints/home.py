from flask import Blueprint, render_template, redirect, request, url_for

home = Blueprint('home', __name__)


@home.route('/')
def home_page():
    return render_template('home/index.html')


@home.route('/lookup', methods=['POST'])
def lookup():
    return redirect(url_for('stock.quote', ticker=request.form['ticker']))

