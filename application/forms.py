from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username=StringField("Name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired()])
    Github=StringField("Github Url",validators=[DataRequired()])
    linkdln=StringField("Linkdln Url",validators=[DataRequired()])
    Tech=StringField("Skills",validators=[DataRequired()])
    submit=SubmitField("Register Now")