import oandapyv20
import oandapyv20.endpoints.pricing as pricing
from oandaconfig import OANDA_ACCESS_TOKEN, OANDA_ACCOUNT_ID

# Connect to OANDA API
api = oandapyv20.API(access_token=OANDA_ACCESS_TOKEN)

# Request real-time prices for EUR/USD
params = {"instruments": "EUR_USD"}
r = pricing.PricingInfo(OANDA_ACCOUNT_ID, params=params)
response = api.request(r)

# Print the latest bid/ask prices
print("EUR/USD Bid Price:", response["prices"][0]["bids"][0]["price"])
print("EUR/USD Ask Price:", response["prices"][0]["asks"][0]["price"])