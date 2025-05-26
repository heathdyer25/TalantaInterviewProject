"""
views.py

Routes for views (webpages) on our website

Author: Heath Dyer
Created: 2025-05-22
"""

from app import app
from app.utils.finance import get_tickers

from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/earnings-relesase-dates')
def earnings_release_dates():
    return render_template('earnings_release_dates.html', tickers=get_tickers())