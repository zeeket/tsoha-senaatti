from flask_wtf import FlaskForm
from wtforms import StringField

class PollForm(FlaskForm):
    name = StringField("Senaatin nimi*")
    description = StringField("Pidempi kuvaus senaatille")
 
    class Meta:
        csrf = False
