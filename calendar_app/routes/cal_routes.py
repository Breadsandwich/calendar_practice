from flask import Blueprint, redirect, render_template
from datetime import datetime
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
        # name = form.data['name']
        # start_date = form.data['start_date']
        # start_time = form.data['start_time']
        # end_date = form.data['end_date']
        # end_time = form.data['end_time']
        # description = form.data['description']
        # private = form.data['private']

        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                    '''
                    INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
                    VALUES (
                        %(name)s,
                        %(start_datetime)s,
                        %(end_datetime)s,
                        %(description)s,
                        %(private)s
                    )
                    ''',
                    {
                        "name": form.name.data,
                        "start_datetime": datetime.combine(form.start_date.data, form.start_time.data),
                        "end_datetime": datetime.combine(form.end_date.data, form.end_time.data),
                        "description": form.description.data,
                        "private": form.private.data,
                    }
                )
        return redirect('/calendar')
    return render_template('new_appointment.html', form=form)
