# Script to update database using Coinbase API

import requests

from flask import jsonify, json
from money.app import app, db
from money.models import Currency

def get_currencies():
	r = requests.get('https://api.coinbase.com/v2/currencies')
	currencies = r.json()['data']

	for curr in currencies:
		if Currency.select().where(Currency.code == curr['id']):
			currency = Currency.get(Currency.code == curr['id'])
			currency.name = curr['name']
			currency.min_size = curr['min_size']
			currency.save()
		else:
			currency = Currency.create(code=curr['id'], name=curr['name'], min_size=curr['min_size'])
			currency.save()

if __name__ == '__main__':
	ctx = app.test_request_context()
	ctx.push()
	get_currencies()