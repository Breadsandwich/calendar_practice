from flask import Blueprint, render_template
import os
import psycopg2

bp = Blueprint('calendar', __name__, url_prefix='/calendar')

# @bp.route("/")
# def test():
#     return render_template('main.html')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route('/')
def main():
    print('hello??')
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            # def get_all_appointments():
            curs.execute(
                """
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime;
                """
            )
            results = curs.fetchall()
        # results = get_all_appointments()
        print('!!!!!!!!!', results)

    return render_template('main.html', rows=results)
