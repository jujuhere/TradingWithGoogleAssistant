import os
import requests


class RequestHandler:
    def __init__(self):
        self.ifttt_url: str = os.environ.get("IFTTT_URL")

    # todo: implement skeleton for the post request
    def post_data(self, value_1: str, value_2: str):
        notification = requests.post(
            self.ifttt_url, params = {'value1':value_1,'value2':value_2})  
        return notification

class IFTTT(RequestHandler):
    def send_notification(self, side: str, quantity: int, symbol: str):
        return_title = 'Lemon.markets ' + ('buy' if side == 'buy' else 'sell') + ' Order Submitted'
        return_body = 'Order to ' + side + ' ' + str(quantity) + ' shares of ' + symbol + ' submitted.'

        return self.post_data(return_title, return_body)
