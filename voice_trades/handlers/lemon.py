import os
import json
import requests

class RequestHandler:
    def __init__(self):
        self.api_key: str = os.environ.get("API_KEY")
        self.url_trading: str = os.environ.get("TRADING_URL")

    # todo: implement; should provide a 'structure' for all subsequent post requests
    def post_data(self, endpoint: str, data: dict):
        response = requests.post(
            self.url_trading + endpoint, json.dumps(data), headers = self.headers)
        return response.json()

class LemonMarketsAPI(RequestHandler):
    # todo: using the post_data method, place an order
    # hint: return order ID
    def place_order(self, isin: str, expires_at: str, side: str, quantity: str, venue: str):
        venue = os.environ.get("MIC")
        
        order_details = {
            "isin" : isin, 
            "expires_at" : expires_at,
            "side": side,
            "quantity" : quantity,
            "venue" : venue
        }
        return self.post_data(f"orders/", order_details)

    # todo: using the post_data method, activate an order
    # hint: return response in json format
    def activate_order(self):
        return self.post_data(
            f"orders/{order_id}/activate/", {}
        )
        
