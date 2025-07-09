import requests
import time
import hmac
import hashlib
from config import API_KEY, API_SECRET
from logger import log_info, log_error

BASE_URL = "https://testnet.binancefuture.com"

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = BASE_URL if testnet else "https://fapi.binance.com"

    def get_signature(self, query_string):
        return hmac.new(self.api_secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            log_info(f"Simulated Order - symbol: {symbol}, side: {side}, type: {order_type}, quantity: {quantity}, price: {price}, stop_price: {stop_price}")
            time.sleep(1)  # Simulate network delay
            simulated_response = {
                "symbol": symbol,
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity,
                "price": price or "market price",
                "stop_price": stop_price or "N/A",
                "status": "FILLED",
                "orderId": int(time.time()),
                "timestamp": int(time.time() * 1000)
            }
            log_info(f"Simulated Response: {simulated_response}")
            return simulated_response
        except Exception as e:
            log_error(str(e))
            return {"error": str(e)}

def main():
    print("Welcome to Simplified Binance Futures Trading Bot")
    symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter side (BUY/SELL): ").strip().upper()
    order_type = input("Enter order type (MARKET/LIMIT/STOP/STOP_LIMIT): ").strip().upper()
    quantity = input("Enter quantity: ").strip()

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP", "STOP_LIMIT"]:
        price = input("Enter price: ").strip()
    if order_type in ["STOP", "STOP_MARKET", "STOP_LIMIT"]:
        stop_price = input("Enter stop price: ").strip()

    bot = BasicBot(API_KEY, API_SECRET)
    result = bot.place_order(symbol, side, order_type, quantity, price, stop_price)
    print("Order Result:", result)

if __name__ == "__main__":
    main()
