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


"""
Returns a hardcoded list of tickers for testing or predefined use.
"""
def get_tickers():
    return [
        "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NVDA",
        "ADBE", "AMD", "ABNB", "AEP", "AMGN", "ADI", "ANSS", "AMAT", "APP",
        "ARM", "ASML", "AZN", "TEAM", "ADSK", "ADP", "AXON", "BKR", "BIIB",
        "BKNG", "AVGO", "CDNS", "CDW", "CHTR", "CMCSA", "CPRT", "CRWD",
        "CSCO", "CTAS", "CTSH", "DDOG", "DLTR", "DXCM", "EA", "EBAY", "ENPH",
        "EXC", "FAST", "FI", "FTNT", "GILD", "HON", "IDXX", "ILMN", "INTC",
        "INTU", "ISRG", "JD", "KDP", "KLAC", "LCID", "LRCX", "MAR", "MCHP",
        "MDLZ", "MELI", "MNST", "MRNA", "MRVL", "MU", "NFLX", "NTES", "NXPI",
        "ODFL", "ORLY", "PANW", "PAYX", "PCAR", "PDD", "PEP", "PYPL", "QCOM",
        "REGN", "ROST", "SBUX", "SIRI", "SNPS", "SWKS", "TMUS", "TXN", "VRSK",
        "VRTX", "WBA", "WDAY", "XEL", "ZM", "ZS", "PLTR", "MSTR", "SHOP",
        "SNOW", "UBER", "ROKU"
    ]

"""
Given a list of ticker symbols, return a dict mapping ticker to its earnings start date as a string.
If no earnings date is found, note that in the dict.
"""
def get_earnings_start_dates(tickers):
    tickers_obj = yf.Tickers(" ".join(tickers))
    data = []
    for ticker in tickers:
        try:
            stock = tickers_obj.tickers[ticker]
            cal = stock.calendar
            if cal is not None and "Earnings Date" in cal:
                earnings_date = str(cal["Earnings Date"][0])
            else:
                earnings_date = "N/A"
        except Exception as e:
            print(f"{ticker}: {e}")
            earnings_date = "N/A"
        
        data.append({
            "ticker": ticker,
            "earnings_date": earnings_date,
        })
    return data