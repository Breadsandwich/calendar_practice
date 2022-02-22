from flask import Flask, render_template
import os

from calendar_app.routes.cal_routes import bp



app = Flask(__name__)
app.config.update({'SECRET_KEY': os.environ.get('SECRET_KEY')})
app.register_blueprint(bp)
