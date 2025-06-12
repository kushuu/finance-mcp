import yfinance
from mcp.server.fastmcp import FastMCP

from zerodha_utils import get_holdings as _get_holdings
from zerodha_utils import get_orders as _get_orders
from zerodha_utils import place_order as _place_order

mcp = FastMCP("finance-assistant-agent")


@mcp.tool()
def get_stock_data(ticker: str, num_days: int):
    """Get stock data from yfinance"""
    ticker = ticker.strip()
    if not ticker:
        return "The ticker must not be empty!"
    if num_days < 1:
        return "The number of days must be at least 1!"

    return yfinance.Ticker(ticker).history(period=f"{num_days}d")

@mcp.tool()
def get_holdings():
    return _get_holdings()

@mcp.tool()
def get_orders():
    return _get_orders()

@mcp.tool()
def place_order(type: str, ticker: str, quantity: int):
    return _place_order(type, ticker, quantity)
