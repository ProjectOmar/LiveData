import oandapyv20
import oandapyv20.endpoints.pricing as pricing
from oandaconfig import ACCESS_TOKEN, ACCOUNT_ID

#Connect
api = oandapyv20.API(access_token=ACCESS_TOKEN)

#Real-time prices
params = {"instruments": "EUR_USD"}
r = pricing.PricingInfo(ACCOUNT_ID, params=params)
response = api.request(r)

#Prints prices
print("EUR/USD Bid Price:", response["prices"][0]["bids"][0]["price"])
print("EUR/USD Ask Price:", response["prices"][0]["asks"][0]["price"])
