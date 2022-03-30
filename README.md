# Use IFTTT and the lemon.markets API to trade in the stock market with services like Google Assistant 
Code Snippet (Incomplete) which is part of the Alexa/Google Home implementation to execute trading on the stock market with Amazon/Google's virutal assistant including the lemon.markets API.

## Instructions for Use
This script can be used as a starting point to implement your own trading service with lemon.markets for your virtual assistant from Amazon or Google.
As you can already see, it only contains the Python code that you can use to upload on AWS.
AWS is an environment which offers cloud computing plattforms for e.g. hosting your IFTTT implementation (the Python file).

You'll receive a step-by-step guide on how to set AWS for the IFTTT implementation by contacting me via email with #lemonmarketsgoesHome written in subject. I'll send you the guideline and will also show my openness for your questions. 

Sign up on AWS [here](https://signin.aws.amazon.com/signin?redirect_uri=https%3A%2F%2Fus-east-1.console.aws.amazon.com%2Flambda%2Fhome%3Fregion%3Dus-east-1%26skipRegion%3Dtrue%26state%3DhashArgs%2523%26isauthcode%3Dtrue&client_id=arn%3Aaws%3Aiam%3A%3A015428540659%3Auser%2Flambda&forceMobileApp=0&code_challenge=-RpLm0z5LIGz3i36lzYlyWGHaOJyhWcLgIOkalmimBs&code_challenge_method=SHA-256). 

By clicking this link below, you'll find a list of regions that you will need for setting up the layer in AWS (you need that to import the request library). You can find your region on the top-right corner of the AWS page (next to your profile). 
* https://github.com/keithrozario/Klayers/tree/master/deployments/python3.9

If you're not sure about how to use the lemon.markets API for the project, I'd recommend you to read the document to learn more about how to implement the lemon.markets API into your projects.
* https://docs.lemon.markets

## Environmental Variables
You'll notice that the script uses several environment variables to include the API. Please define the following in an .env file or within your IDE:

- API_KEY - Your lemon.markets API key
- stock_dict - Add the [stocks](https://www.boerse-muenchen.de/home) you'd like to buy/sell with Virtual Assistants into dictionary (left side: stockname & right side: ISIN, e.g. Nintendo : JP3756600007 )

## Configuration

The script uses several environment variables, configure your .env file as follows:

```python
TRADING_URL=https://paper-trading.lemon.markets/v1/
API_KEY=<your-api-key>
IFTTT_URL= https://maker.ifttt.com/trigger/market_closed/with/key/{KEY}
```
Please provide your unique `API_KEY`. 

## Interested in contributing?
This (and all lemon.markets open source projects) is work in progress. 
If you are interested in contributing to this repository, simply create a PR and/or contact the team of lemon.markets at support@lemon.markets.
To learn more about the use of the IFTTT, Google Assistants or the use of the lemon.markets API, feel free to contact me (julian.gabenstein@lemon.markets) and I'll send you the presentation with a step-by-step guide to make your first steps with the AWS console and the API as easy as possible. 

Looking forward to building lemon.markets with you 🍋
