from flask import Flask
# import psycopg2
from calendar_app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return 'from app'
