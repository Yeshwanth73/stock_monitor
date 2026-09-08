import yfinance as yf
from datetime import datetime

def get_stock_price(ticker: str):
    """
    Fetches the latest stock price for a given ticker symbol.
    Uses Yahoo Finance via yfinance library.
    """
    try:
        if not ticker or not isinstance(ticker, str):
            raise ValueError("Ticker must be a non-empty string.")

        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")  # Today's data

        if data.empty:
            raise ValueError(f"No data found for ticker '{ticker}'.")

        latest_price = data['Close'].iloc[-1]
        print(f"{ticker.upper()} latest closing price: ${latest_price:.2f} (as of {datetime.now().date()})")
        return latest_price

    except Exception as e:
        print(f"Error fetching stock price: {e}")
        return None

if __name__ == "__main__":
    # Example: Apple Inc.
    get_stock_price("AAPL")
    # Example: Tesla
    get_stock_price("TSLA")