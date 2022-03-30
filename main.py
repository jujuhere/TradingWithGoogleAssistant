from voice_trades import helpers
from voice_trades.handlers.ifttt import IFTTT
from voice_trades.handlers.lemon import LemonMarketsAPI


def lambda_handler(event, context):

    lemon_api: LemonMarketsAPI = LemonMarketsAPI()
    ifttt_handler: IFTTT = IFTTT()

    # interpret voice input
    symbol = event['symbol'].upper().split(' ')[
        -1]  # get the last word from voice input, in case extra words are detected
    try:
        quantity = int(event['quantity'])  # this will work if the voice input for quantity is detected in number form
    except:
        quantity = helpers.text2int(
            event['quantity'])  # this will be used if the voice input for quantity is detected in word form

    # stock dictionary
    stock_dicts = {
        "NINTENDO": "JP3756600007",
        "SPOTIFY": "LU1778762911",
        "PAYPAL": "CA70452C1095"
    }

    # todo : insert parameters into place_order method
    order = lemon_api.place_order()
    activated_order = lemon_api.activate_order(order)

    ifttt_handler.send_notification(event['action'], quantity, symbol)

    return {
        'statusCode': 200,
        'body': activated_order
    }