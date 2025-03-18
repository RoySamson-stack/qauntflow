import os 


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False


# change this 
JWT_SECRET_KEY = 'super-secret'

# change this 
ALPHA_VANTAGE_API = "my_api"
BINANCE_API_KEY = "binance_api"