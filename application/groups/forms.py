from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SelectMultipleField, SubmitField,

class GroupForm(FlaskForm):
    name = StringField("Ryhmän nim", [validators.Length(min=3)])
    group_users_select = SelectMultipleField(label='Users')
    class Meta:
        csrf = False
