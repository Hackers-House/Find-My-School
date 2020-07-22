from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username=StringField("Name",validators=[DataRequired()])
    email=StringField("Email",validators=[DataRequired()])
    Guthub_url=StringField("Github Url",validators=[DataRequired()])
    linkdln_Url=StringField("Linkdln Url",validators=[DataRequired()])
    Technologies=StringField("Skills",validators=[DataRequired()])
    submit=SubmitField("Register Now")