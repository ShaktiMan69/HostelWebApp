from wtforms import StringField, FileField, IntegerField, EmailField
from flask_wtf import FlaskForm
from wtforms.validators import Email, InputRequired

# Define a WTForm class for the registration form
class RegistrationForm(FlaskForm):
    # Page 1
    name = StringField('Name', validators=[InputRequired(), ])
    address = StringField('Address', validators=[InputRequired()])
    distance = IntegerField('Distance (KM)', validators=[InputRequired()])
    phone = IntegerField('Mobile Number', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    parent_name = StringField("Parent's Name", validators=[InputRequired()])
    parent_phone = IntegerField("Parent's Mobile Number", validators=[InputRequired()])
    # Page 2
    year = IntegerField('Year', validators=[InputRequired()])
    semester = StringField('Semester', validators=[InputRequired()])
    pr_number = IntegerField('PR Number', validators=[InputRequired()])
    department = StringField('Department', validators=[InputRequired()])
    photo = FileField('Upload Photo ')
    id_proof = FileField('Upload ID Proof (PDF) ')