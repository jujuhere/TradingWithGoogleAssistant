import os
import requests


class RequestHandler:
    def __init__(self):
        self.ifttt_url: str = os.environ.get("IFTTT_URL")

    # todo: implement skeleton for the post request
    def post_data(self, value_1: str, value_2: str):
        notification = requests.post(
            self.ifttt_url + endpoint, params = {'value1':return_title,'value2':return_body}) # i think params = self.params doesn't make sense 
        return notification 

class IFTTT(RequestHandler):
    def send_notification(self, side: str, quantity: int, symbol: str):
        return_title = 'Lemon.markets ' + ('buy' if side == 'buy' else 'sell') + ' Order Submitted'
        return_body = 'Order to ' + side + ' ' + str(quantity) + ' shares of ' + symbol + ' submitted.'

        post_data(return_title, return_body)
