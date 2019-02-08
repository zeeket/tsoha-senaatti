from flask_wtf import FlaskForm
from wtforms import StringField,validators

class GroupForm(FlaskForm):
    name = StringField("Ryhmän nimi*", [validators.Length(min=3)])
#tähän tulee käyttäjien vaa ryhmään

class Meta:
        csrf = False
