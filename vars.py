import os
from dotenv import load_dotenv

load_dotenv('.env')


DB_URL = os.environ.get('DB_URL')
SLACK_API_KEY = os.environ.get('SLACK_API_KEY')

WALLET_NAME = os.environ.get("WALLET_NAME")

print(os.environ)
