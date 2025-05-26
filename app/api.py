"""
api.py

This module provides API calls, primarily using yfinance data.

Author: Heath Dyer
Created: 2025-05-22
"""

from app import app

from flask import Blueprint, jsonify, request
from app.utils.finance import get_earnings_start_dates, get_tickers

# Create new blueprint with api prefix
api = Blueprint("api", __name__, url_prefix="/api")

# Harcoded list of tickers
@api.route('/tickers', methods=['GET'])
def get_tickers_api():
    return jsonify(get_tickers()), 200

# API call to retireve 
@api.route('/earnings-release-dates', methods=['POST'])
def get_earnings_start_dates_api():
    data = request.get_json()
    tickers = data.get('tickers', [])

    if not isinstance(tickers, list) or not tickers:
        return jsonify({'error': 'Please provide a list of tickers.'}), 400

    results = get_earnings_start_dates(tickers)
    return jsonify(results), 200

# Add API blueprint to app
app.register_blueprint(api)