from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
from application.auth.models import User

  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjänimi")
    password = PasswordField("Salasana")
  
    class Meta:
        csrf = False

def user_exists_check(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('Valitsemasi käyttäjänimi on jo käytössä')

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjänimi", [validators.DataRequired(), validators.Length(min=3), user_exists_check])
    password = PasswordField("Salasana", [validators.DataRequired(), validators.Length(min=6), validators.EqualTo('passwordagain', message='Salasanojen on oltava samat')])
    passwordagain = PasswordField("Salasana uudelleen")
 
    class Meta:
        csrf = False
