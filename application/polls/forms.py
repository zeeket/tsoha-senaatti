from flask_wtf import FlaskForm
from wtforms import StringField,validators, SubmitField

class PollForm(FlaskForm):
    name = StringField("Senaatin nimi*", [validators.Length(min=3,max=30)])
    description = StringField("Pidempi kuvaus senaatille", [validators.Length(max=78)])

    class Meta:
        csrf = False
"""
class SinglePollForm(FlaskForm):
    upvote = SubmitField()
    neutralvote = SubmitField()
    downvote = SubmitField()
"""

