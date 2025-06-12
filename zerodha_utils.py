import os

from dotenv import load_dotenv
from kiteconnect import KiteConnect

load_dotenv()

API_KEY = os.getenv("ZERODHA_API_KEY")
kite_obj = KiteConnect(api_key=API_KEY)
kite_obj.set_access_token(os.getenv("ZERODHA_ACCESS_TOKEN"))


def get_holdings():
    holdings = kite_obj.holdings()
    return holdings


def get_orders():
    orders = kite_obj.orders()
    return orders


def place_order(type: str, ticker: str, quantity: int):
    order = kite_obj.place_order(
        variety="regular",
        exchange="NSE",
        tradingsymbol=ticker,
        transaction_type=type,
        quantity=quantity,
        product="MIS",
        order_type="MARKET",
        validity="DAY",
    )
    return order
