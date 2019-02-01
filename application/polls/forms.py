from flask_wtf import FlaskForm
from wtforms import StringField,validators

class PollForm(FlaskForm):
    name = StringField("Senaatin nimi*", [validators.Length(min=3)])
    description = StringField("Pidempi kuvaus senaatille")
 
    class Meta:
        csrf = False
