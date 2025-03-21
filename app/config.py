import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_SECRET_KEY = 'your-secret-key-here'

ALPHA_VANTAGE_API_KEY = 'QF87ZGPNIUDNLQWV'
BINANCE_API_KEY = 'your-binance-api-key'