from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, DateField, TimeField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class NewAppointment(FlaskForm):
    name = StringField('Name')
    start_date = DateField('Start Date')
    start_time = TimeField('Start Time')
    end_date = DateField('End Date')
    end_time = TimeField('End Time')
    description = TextAreaField('Description')
    private = BooleanField('Private')
    submit = SubmitField('Submit Appointment')
