"""
finance.py

This module provides functions to interact with yfinance API,
retrieve stock data, and process earnings release dates.

Author: Heath Dyer
Created: 2025-05-22
"""

import yfinance as yf
import pandas as pd
from datetime import datetime

#File for 

"""
Returns a hardcoded list of tickers for testing or predefined use.
"""
def get_tickers():
    return [
        "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
        "META", "NVDA", "JPM", "V", "JNJ",
        "WMT", "PG", "MA", "DIS", "HD",
        "BAC", "PEP", "KO", "XOM", "NFLX"
    ]

"""
Given a list of ticker symbols, return a dict mapping ticker to its earnings start date as a string.
If no earnings date is found, note that in the dict.
"""
def get_earnings_start_dates(tickers):
    data = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        try:
            cal = stock.calendar
            if cal:
                earnings_date = str(cal["Earnings Date"][0])
            else:
                raise Exception('calendar not found')
        except Exception as e:
            print(e)
            earnings_date = 'N/A'
        data.append({
            "ticker": ticker,
            "earnings_date": earnings_date,
        })
    return data