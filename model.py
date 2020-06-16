from flask_wtf import FlaskForm
from wtforms.fields import IntegerField
from wtforms.validators import AnyOf


class SingleIntegerInput(FlaskForm):
    inputInt = IntegerField('YourInteger', validators=[AnyOf(range(-10000, 10000))])
