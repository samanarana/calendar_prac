from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, TextAreaField, TimeField, DateField, StringField, SubmitField
)
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    start_date = DateField("Start", validators=[DataRequired()])
    start_time = TimeField("Start", validators=[DataRequired()])
    end_date = DateField("End", validators=[DataRequired()])
    end_time = TimeField("End", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    private = BooleanField("Private")
    submit = SubmitField('Create an Appointment')
