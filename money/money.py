from money.app import app, db
from money.views import *
from money.models import Currency, Rate, Order

def create_tables():
	db.connect()
	db.create_tables([Currency, Rate, Order], safe=True)
	db.close()

create_tables()

if __name__ == '__main__':
    app.run()
