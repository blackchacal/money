from .app import app, db
from .views import *
from .models import *

def create_tables():
	db.connect()
	db.create_tables([Currency, Rate, Order], safe=True)
	db.close()

if __name__ == '__main__':
    create_tables()
    app.run()
