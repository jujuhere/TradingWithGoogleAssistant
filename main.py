from voice_trades import helpers
from voice_trades.handlers.lemon import LemonMarketsAPI


def lambda_handler(event, context):

    lemon_api: LemonMarketsAPI = LemonMarketsAPI()

    # interpret voice input
    symbol = event['symbol'].upper().split(' ')[
        -1]  # get the last word from voice input
    try:
        quantity = int(event['quantity'])  # voice input for quantity is detected in number form
    except:
        quantity = helpers.text2int(
            event['quantity'])  # voice input for quantity is detected in word form

    # stock dictionary (add your stocks that you'd like to trade; you can also add your stock manually in Zapier's webhooks) 
    stock_dicts = {
        "NINTENDO": "JP3756600007",
        "SPOTIFY": "LU1778762911",
        "PAYPAL": "CA70452C1095"
    }

    # todo : insert parameters into place_order method 
    # (tip if not working: change symbol into number to call a specific key of the dictionary + change event into "buy" or "sell" + change quantiy into a number) 
    order = lemon_api.place_order(stock_dicts[symbol], "2022-05-30", event['action'], quantity, "XMUN")
    activated_order = lemon_api.activate_order(order.get("results").get("id"))


    return {
        'statusCode': 200,
        'body': activated_order
    }
