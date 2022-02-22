from flask import Blueprint, render_template

bp = Blueprint('calendar', __name__, url_prefix='/calendar')

@bp.route("/")
def test():
    return render_template('main.html')
