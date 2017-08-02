import datetime

from peewee import *
from money.app import db

class BaseModel(Model):
	class Meta:
		database = db

# Currency model
class Currency(BaseModel):
	code = CharField(unique=True, max_length=3)
	name = CharField()
	min_size = FloatField()
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)

	def rates():
		return (Currency
				.select()
				.join(Rate, on=Rate.base_currency)
				.where(Rate.base_currency == self))

	def rate_by_currency(currency):
		return (Currency
				.select()
				.join(Rate, on=Rate.base_currency)
				.where(Rate.base_currency == self & Rate.exchange_currency == currency))

class Rate(BaseModel):
	base_currency = ForeignKeyField(Currency, related_name='rates')
	exchange_currency = CharField(unique=True, max_length=3)
	rate = FloatField()
	created_at = DateTimeField(default=datetime.datetime.now)
	updated_at = DateTimeField(default=datetime.datetime.now)

class Order(BaseModel):
	type = CharField(max_length=10)
	currency_pair = CharField(max_length=7)
	amount = FloatField()
	price = FloatField()
	created_at = DateTimeField(default=datetime.datetime.now)

db.connect()
db.close()