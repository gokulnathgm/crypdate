import urllib2, json
from twilio.rest import Client
from config import *


response = urllib2.urlopen('https://api.coinmarketcap.com/v1/ticker/ripple/?convert=INR')

response_str = response.read()
response_str = response_str.replace(' ', '')
data = response_str.split('\n')

for i in data:
	if i.startswith('"price_inr"'):
		price = i
		break

price = price.split(":")[1]
price = price.replace('"', '')
price = price.replace(',', '')
print '\nActual price: ', price,
price = float(price) + 22
print '\nExchange price: ', price, '\n'

response.close()

msg_body = "Price of Ripple is: " + str(price)


client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to=to_number,
                                             from_=from_number,
                                             body=msg_body)
print message.sid