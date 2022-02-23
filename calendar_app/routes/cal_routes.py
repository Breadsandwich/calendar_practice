from flask import Blueprint, redirect, render_template
import os
import psycopg2
from calendar_app.forms import NewAppointment

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


@bp.route('/new_appointment', methods=['GET','POST'])
def new_appoint():
    form = NewAppointment()

    if form.validate_on_submit():
        name = form.data['name']
        start_date = form.data['start date']
        start_time = form.data['start time']
        end_date = form.data['end date']
        end_time = form.data['end time']
        description = form.data['description']
        private = form.data['private']

        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                    '''
                    INSERT INTO appointments (name, start_date, start_time, end_date, end_time, description, private)
                    VALUES (
                        %(name)s,
                        %(start_date)s,
                        %(start_time)s,
                        %(end_date)s,
                        %(end_time)s,
                        %(description)s,
                        %(private)s
                    )
                    ''',
                    {
                        "name": name,
                        "start_date": start_date,
                        "start_time": start_time,
                        "end_date": end_date,
                        "end_time": end_time,
                        "description": description,
                        "private": private,
                    }
                )
        return redirect('/calendar')
    return render_template('main.html', form=form)
